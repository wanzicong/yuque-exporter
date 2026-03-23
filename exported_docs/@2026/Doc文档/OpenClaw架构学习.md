# OpenClaw 核心Agent架构分析
## 1. 核心入口点
| 文件 | 行号 | 职责 |
| --- | --- | --- |
| src/gateway/server-methods/agent.ts | 148 | Gateway RPC入口 |
| src/commands/agent.ts | - | CLI命令入口 |
| src/agents/agent-command.ts | 1221 | 核心agentCommand函数 |


## 2. 执行流程
```plain
用户请求 → Gateway RPC → agentCommandFromIngress → agentCommandInternal
     ↓
   ├─ 准备执行环境 (prepareAgentCommandExecution)
   ├─ 模型选择和fallback处理 (runWithModelFallback)
   └─ runEmbeddedPiAgent
        ↓
     ├─ 队列处理 (enqueueSession/enqueueGlobal)
     ├─ 创建Agent Session
     ├─ 订阅事件 (subscribeEmbeddedPiSession)
     └─ 执行工具调用
```

## 3. 核心组件
### 消息处理
+ **文件**: src/agents/pi-embedded-subscribe.ts:34
+ **功能**: 状态管理、文本块处理、重复检测、消息工具去重

### 工具调用
+ **文件**: src/agents/pi-tools.before-tool-call.ts:89
+ **功能**: 
    - 执行前钩子: runBeforeToolCallHook
    - 循环检测: detectToolCallLoop
    - 工具结果处理: emitToolResultMessage

### 状态管理
+ Session Lane队列 (串行执行 + 可选全局队列)
+ Subagent运行记录 (subagentRuns)
+ 生命周期事件 (emitAgentEvent)

### 错误处理
+ 模型回退: runWithModelFallback
+ 重试迭代: 最多160次重试
+ 上下文窗口守卫: evaluateContextWindowGuard

## 4. 架构模式
### 插件钩子系统
+ **文件**: src/plugins/hooks.ts:11-55
+ **核心钩子**: 
    - before_model_resolve
    - before_prompt_build
    - before_agent_start
    - before_tool_call
    - after_tool_call

### 队列和并发控制
+ **文件**: src/process/command-queue.ts
+ **三种模式**: collect(收集), steer(转向), followup(跟进)

### 上下文压缩(Compaction)
+ **文件**: src/agents/pi-embedded-runner/compact.ts
+ **触发条件**: 上下文窗口溢出、工具结果过大、token限制

## 5. 数据流总结
```plain
输入 → 参数验证 → 模型选择 → 队列等待 → 工作区准备
    → System Prompt → Agent Session → 事件循环(推理/工具/压缩)
    → 结果聚合 → Transcript持久化 → 结果传递
```

**架构特点**: 模块化、可扩展、完善的容错机制(重试/fallback/压缩)、丰富的钩子点用于扩展。

---

# OpenClaw 系统内置工具
## 一、基础Coding工具 (来自 @mariozechner/pi-coding-agent)
| 工具名 | 描述 |
| --- | --- |
| read | 读取文件内容 |
| write | 写入文件 |
| edit | 编辑文件 |
| bash | 执行Shell命令 |
| apply_patch | 应用代码补丁 |


## 二、OpenClaw核心工具
### 浏览器相关
| 工具名 | 描述 |
| --- | --- |
| browser | 浏览器控制（自动化网页操作） |


### Canvas/绘图
| 工具名 | 描述 |
| --- | --- |
| canvas | Canvas绘图工具 |


### 定时任务
| 工具名 | 描述 |
| --- | --- |
| cron | 定时任务管理 |


### 网关/Agent管理
| 工具名 | 描述 |
| --- | --- |
| gateway | 网关控制工具 |
| agents_list | 列出所有Agent |
| subagents | Subagent管理 |


### 消息/通信
| 工具名 | 描述 |
| --- | --- |
| message | 发送消息（支持多平台） |
| tts | 文字转语音 |


### Web搜索/获取
| 工具名 | 描述 |
| --- | --- |
| web_search | 网络搜索 |
| web_fetch | 网页抓取 |


### 图像处理
| 工具名 | 描述 |
| --- | --- |
| image | 图像理解/分析 |
| image_generate | 图像生成 |


### PDF处理
| 工具名 | 描述 |
| --- | --- |
| pdf | PDF读取处理 |


### 会话管理
| 工具名 | 描述 |
| --- | --- |
| sessions_list | 列出所有会话 |
| sessions_history | 获取会话历史 |
| sessions_send | 发送消息到会话 |
| sessions_spawn | 创建新会话 |
| sessions_yield | 暂停当前会话 |
| session_status | 获取会话状态 |


### 节点/Nodes
| 工具名 | 描述 |
| --- | --- |
| nodes | 节点操作工具 |


### 执行相关
| 工具名 | 描述 |
| --- | --- |
| exec | 执行Shell命令（安全版本） |
| process | 进程管理 |


## 三、工具来源架构
```plain
工具创建入口: src/agents/pi-tools.ts (createOpenClawCodingTools)
     ↓
1. 基础Coding工具: @mariozechner/pi-coding-agent
     - read, write, edit, bash, apply_patch

2. 自定义工具: src/agents/openclaw-tools.ts
     - browser, canvas, cron, gateway, message, tts
     - web_search, web_fetch, image, image_generate, pdf
     - sessions_*, agents_list, subagents, nodes

3. 插件工具: src/plugins/tools.ts
     - 通过 resolvePluginTools 动态加载
```

## 四、工具策略控制
+ **Tool Policy Pipeline**: 支持基于profile、provider、group、agent的细粒度控制
+ **Sandbox**: 支持沙箱环境下的工具限制
+ **Subagent**: 支持子Agent的工具权限隔离

---

# OpenClaw Agent 运行机制
## 结论：不是 ReAct，而是基于 pi-agent-core 的流式事件驱动循环
OpenClaw 的 agent 运行机制**不是 ReAct 模式**，而是一种流式事件驱动的 Agent Loop 模式。

---

## 架构核心
```plain
┌─────────────────────────────────────────────────────────────┐
│                    pi-agent-core                             │
│  (@mariozechner/pi-agent-core v0.58.0)                      │
│                                                              │
│  核心职责：                                                  │
│  - Agent Loop (循环执行)                                      │
│  - 工具执行管理                                              │
│  - AgentMessage 类型定义                                      │
└─────────────────────────────────────────────────────────────┘
```

---

## 执行流程（不是 ReAct）
### 1. 入口点
+ Gateway RPC: agent / agent.wait
+ CLI: agent 命令

### 2. 核心执行链
```plain
agent.ts:148 (RPC入口)
     ↓
agentCommand.ts:1221 (主命令函数)
     ↓
runEmbeddedPiAgent (pi-agent-core运行时)
     ↓
runEmbeddedAttempt (单次执行尝试)
     ↓
subscribeEmbeddedPiSession (事件订阅处理)
```

### 3. Agent Loop 核心模式（代码层面）
```typescript
// run.ts:886 - 重试循环
while (true) {
  if (runLoopIterations >= MAX_RUN_LOOP_ITERATIONS) break;

  // 执行单次尝试
  const attempt = await runEmbeddedAttempt({
    // ...参数
  });

  // 上下文溢出处理 → 压缩重试
  if (attempt.hasOverflow) {
    await contextEngine.compact();
    continue; // 重试
  }

  // 正常结束
  break;
}
```

---

## 与 ReAct 的区别
| 特性 | ReAct 模式 | OpenClaw (pi-agent-core) |
| --- | --- | --- |
| 推理方式 | 显式 thought/action 交替 | 隐式流式推理 |
| 工具调用 | 同步交替 (Thought → Action → Observation) | 异步事件流 |
| 循环控制 | 显式循环次数限制 | 事件驱动 + 超时控制 |
| 输出方式 | 逐步输出 | 流式增量输出 |
| 状态管理 | 显式 reasoning trace | Session 持久化 |


---

## 关键特性
### 1. 流式事件驱动
```typescript
// 事件类型
- lifecycle: start | end | error
- assistant: 增量文本流
- tool: tool_start | tool_delta | tool_end
- compaction: 压缩事件
```

### 2. 工具执行循环
```plain
模型推理 → 工具调用 → 工具结果 → 模型推理 → ...
      ↑                              │
      └──────────────────────────────┘
```

### 3. 上下文管理
+ **自动压缩**: 上下文溢出时触发
+ **重试机制**: 最多 160 次重试
+ **Session 隔离**: 每个会话串行执行

### 4. 队列控制
+ **Session Lane**: 按会话键序列化
+ **全局队列**: 可选的全局通道
+ **模式**: collect / steer / followup

---

## 总结
OpenClaw 使用的是 pi-agent-core 提供的流式事件驱动 Agent Loop，它：

1. ✅ **不是 ReAct** - 不显式输出 thought/action 交替
2. ✅ **流式输出** - 实时流式传输增量文本
3. ✅ **事件驱动** - 通过事件订阅处理各种状态
4. ✅ **自动工具循环** - 模型自主决定调用工具的时机和次数
5. ✅ **上下文管理** - 内置压缩和重试机制

---

# OpenClaw 系统模块划分与依赖关系
## 一、核心模块（按层次）
```plain
┌─────────────────────────────────────────────────────────────────┐
│                      入口层 (Entry)                              │
│  entry.ts / index.ts                                           │
└─────────────────────────────────────────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────────┐
│                    Gateway 网关层                               │
│  gateway/         - HTTP/WebSocket RPC 服务                      │
│  cli/             - 命令行接口                                   │
│  tui/             - 终端用户界面                                 │
└─────────────────────────────────────────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────────┐
│                    Agent 核心层                                  │
│  agents/          - Agent 循环、执行、工具管理                   │
│  context-engine/  - 上下文管理、压缩                             │
│  sessions/        - 会话管理、持久化                             │
│  plugins/         - 插件系统                                     │
│  hooks/           - 钩子系统                                     │
└─────────────────────────────────────────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────────┐
│                    工具层 (Tools)                               │
│  browser/         - 浏览器自动化                                │
│  image-generation/- 图像生成                                    │
│  web-search/      - Web 搜索                                    │
│  secrets/         - 密钥管理                                    │
│  process/         - 进程管理                                    │
└─────────────────────────────────────────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────────┐
│                    消息通道层 (Channels)                        │
│  channels/        - 多平台消息集成 (Slack/Discord/Telegram...)  │
│  auto-reply/     - 自动回复                                    │
│  cron/           - 定时任务                                     │
└─────────────────────────────────────────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────────┐
│                    基础设施层                                   │
│  config/         - 配置管理                                     │
│  infra/          - 基础设施                                     │
│  providers/      - 模型提供商 (OpenAI/Anthropic/Google...)      │
│  security/       - 安全                                         │
│  logging/       - 日志                                         │
│  utils/          - 工具函数                                     │
└─────────────────────────────────────────────────────────────────┘
```

---

## 二、详细模块说明
| 模块 | 目录 | 职责 |
| --- | --- | --- |
| gateway | src/gateway/ | HTTP/WebSocket RPC 服务入口 |
| cli | src/cli/ | 命令行接口 |
| tui | src/tui/ | 终端 UI |
| agents | src/agents/ | Agent 循环、工具执行、订阅处理 |
| context-engine | src/context-engine/ | 上下文压缩、会话管理 |
| sessions | src/sessions/ | 会话持久化、Transcript |
| plugins | src/plugins/ | 插件系统、工具注册 |
| hooks | src/hooks/ | 内部钩子 |
| browser | src/browser/ | Playwright 浏览器自动化 |
| image-generation | src/image-generation/ | 图像生成 (DALL-E/Stable Diffusion) |
| web-search | src/web-search/ | Web 搜索 |
| secrets | src/secrets/ | 密钥管理 |
| process | src/process/ | 命令队列、进程管理 |
| channels | src/channels/ | 多平台消息集成 |
| auto-reply | src/auto-reply/ | 自动回复系统 |
| cron | src/cron/ | 定时任务 |
| config | src/config/ | 配置解析 |
| providers | src/providers/ | AI 模型提供商适配 |
| security | src/security/ | 安全、审计 |
| logging | src/logging/ | 日志系统 |
| infra | src/infra/ | 基础设施 |


---

## 三、模块依赖关系图
```plain
                     ┌─────────────┐
                     │   entry     │
                     └──────┬──────┘
                            │
             ┌──────────────┼──────────────┐
             │              │              │
       ┌─────▼─────┐ ┌─────▼─────┐ ┌─────▼─────┐
       │   cli     │ │  gateway  │ │   tui     │
       └─────┬─────┘ └─────┬─────┘ └─────┬─────┘
             │              │              │
             └──────────────┼──────────────┘
                            │
                     ┌──────▼──────┐
                     │   agents    │
                     └──────┬──────┘
                            │
         ┌──────────────────┼──────────────────┐
         │                  │                  │
    ┌────▼────┐      ┌─────▼─────┐    ┌─────▼─────┐
    │plugins  │      │context-    │    │ sessions  │
    │hooks    │      │engine     │    │           │
    └────┬────┘      └─────┬─────┘    └─────┬─────┘
         │                  │                  │
         │           ┌──────▼──────┐           │
         │           │   tools     │           │
         │           │ (browser,   │           │
         │           │  web-search,│           │
         │           │  image-gen) │           │
         │           └──────┬──────┘           │
         │                  │                  │
    ┌────▼────────────┐    │            ┌─────▼─────┐
    │  channels       │◄───┘            │  config   │
    │  auto-reply     │                  │  providers│
    │  cron           │                  │  security │
    └─────────────────┘                  └───────────┘
```

---

## 四、核心依赖
### 外部核心依赖
```json
{
  "@mariozechner/pi-agent-core": "0.58.0",  // Agent 循环核心
  "@mariozechner/pi-ai": "0.58.0",           // AI 流处理
  "@mariozechner/pi-coding-agent": "0.58.0",  // Coding 工具
  "@anthropic-ai/sdk": "最新",                // Anthropic API
  "openai": "最新",                           // OpenAI API
  "playwright": "最新"                        // 浏览器自动化
}
```

### 内部依赖流向
```plain
config → providers → agents → sessions → channels
   ↓        ↓         ↓        ↓
  infra   logging   plugins  auto-reply
   ↓                            ↓
  security                     cron
```

---

## 五、关键调用链
```plain
用户请求
     ↓
gateway/cli/tui (入口)
     ↓
agents (Agent 循环)
     ↓
 ├── plugins (获取工具)
 ├── context-engine (上下文管理)
 ├── tools (browser/web-search/image-generation)
     ↓
sessions (持久化)
     ↓
channels (消息发送)
```

这个架构是一个**分层的微内核架构**，核心是 Agent 循环，外围通过插件和通道适配各种外部服务。

---

# 模型管理核心模块
## 1. agents 模块（核心）
| 文件 | 职责 |
| --- | --- |
| model-catalog.ts | 模型目录/注册表 |
| model-selection.ts | 模型选择逻辑 |
| model-auth.ts | 模型认证 |
| model-fallback.ts | 模型回退机制 |
| model-ref-profile.ts | 模型引用配置 |
| models-config.ts | 模型配置管理 |
| models-config.providers.ts | 各提供商配置 |


## 2. commands/models 模块（CLI）
| 文件 | 职责 |
| --- | --- |
| list.ts | 列出可用模型 |
| list.registry.ts | 模型注册表 |
| set.ts | 设置默认模型 |
| auth.ts | 模型认证配置 |


## 3. providers 模块（提供商支持）
| 文件 | 职责 |
| --- | --- |
| github-copilot-models.ts | GitHub Copilot 模型 |
| kilocode-shared.ts | Kilocode 支持 |


---

## 模型管理功能
```plain
┌─────────────────────────────────────────────────────────────┐
│                    模型管理 (agents)                         │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐   │
│  │ model-catalog│  │model-selection│ │ model-auth     │   │
│  │  模型目录   │  │   模型选择   │  │   模型认证     │   │
│  └─────────────┘  └─────────────┘  └─────────────────┘   │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐   │
│  │model-fallback│ │ models-config │ │model-ref-profile│   │
│  │   模型回退   │  │   模型配置   │  │   模型引用     │   │
│  └─────────────┘  └─────────────┘  └─────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                             ↑
                             │
┌─────────────────────────────────────────────────────────────┐
│              CLI 模型命令 (commands/models)                  │
│   list / set / auth                                         │
└─────────────────────────────────────────────────────────────┘
```

---

## 支持的模型提供商
在 `models-config.providers.ts` 中定义：

+ **OpenAI** (GPT-4, GPT-4o, o1, o3-mini)
+ **Anthropic** (Claude 3.5/3.7/3.9 Sonnet, Opus)
+ **Google** (Gemini 1.5/2.0)
+ **OpenAI Codex**
+ **xAI** (Grok)
+ **Ollama** (本地模型)
+ **Azure OpenAI**
+ **GitHub Copilot**
+ **Kilocode**
+ **Moonshot** (月之暗面)
+ **MiniMax**
+ **Volcengine BytePlus**
+ **Nvidia**
+ **Cloudflare AI Gateway**
+ **Vercel AI Gateway**

---

## 总结
| 层级 | 模块 | 职责 |
| --- | --- | --- |
| 核心层 | agents/ | 模型选择、认证、回退、配置 |
| CLI层 | commands/models | 用户交互（list/set/auth） |
| 提供商层 | providers/ | 各平台认证集成 |




# OpenClaw 系统设计架构图
## 一、整体架构分层图
<!-- 这是一个文本绘图，源码为：graph TB
    subgraph "用户接入层"
        CLI[CLI命令行接口]
        Gateway[Gateway网关<br/>HTTP/WebSocket RPC]
        TUI[终端UI]
    end

    subgraph "核心处理层"
        AgentCore[Agent核心引擎<br/>pi-agent-core]
        ContextEngine[上下文管理引擎<br/>压缩/重试]
        SessionMgr[会话管理器<br/>Session Lane队列]
        PluginSystem[插件系统<br/>钩子机制]
        
        subgraph "Agent执行流"
            direction LR
            Queue[队列控制<br/>collect/steer/followup]
            Loop[事件驱动循环]
            Tools[工具调用]
        end
    end

    subgraph "工具层"
        CodingTools[基础Coding工具<br/>read/write/edit/bash]
        BrowserTool[浏览器自动化<br/>Playwright]
        ImageTools[图像处理<br/>理解/生成]
        WebTools[网络工具<br/>搜索/抓取]
        MessageTools[消息工具<br/>多平台发送/TTS]
        SessionTools[会话管理工具<br/>list/history/spawn]
    end

    subgraph "模型管理层"
        ModelCatalog[模型目录<br/>Catalog/Registry]
        ModelSelector[模型选择器<br/>Selection/Fallback]
        ProviderAdapter[提供商适配<br/>OpenAI/Anthropic/Google等]
        AuthManager[认证管理]
    end

    subgraph "基础设施层"
        Config[配置管理]
        Logging[日志系统]
        Security[安全审计]
        Storage[持久化存储<br/>Transcript]
    end

    subgraph "外部集成层"
        Channels[消息通道<br/>Slack/Discord/Telegram]
        Cron[定时任务]
        AutoReply[自动回复]
    end

    %% 连接关系
    CLI --> AgentCore
    Gateway --> AgentCore
    TUI --> AgentCore
    
    AgentCore --> ContextEngine
    AgentCore --> SessionMgr
    AgentCore --> PluginSystem
    AgentCore --> Queue
    AgentCore --> Loop
    AgentCore --> Tools
    
    Tools --> CodingTools
    Tools --> BrowserTool
    Tools --> ImageTools
    Tools --> WebTools
    Tools --> MessageTools
    Tools --> SessionTools
    
    AgentCore --> ModelSelector
    ModelSelector --> ModelCatalog
    ModelSelector --> ProviderAdapter
    ModelSelector --> AuthManager
    
    AgentCore --> Config
    AgentCore --> Logging
    AgentCore --> Security
    SessionMgr --> Storage
    
    AgentCore --> Channels
    AgentCore --> Cron
    AgentCore --> AutoReply -->
![](https://cdn.nlark.com/yuque/__mermaid_v3/3a36f63c35f9dc6afbedecedb6a980fe.svg)

## 二、Agent执行流程时序图
<!-- 这是一个文本绘图，源码为：sequenceDiagram
    participant User as 用户
    participant Gateway as Gateway入口
    participant AgentCmd as Agent命令处理器
    participant Queue as 队列管理器
    participant Session as Agent会话
    participant Model as 模型选择器
    participant Tools as 工具执行器
    participant Context as 上下文引擎

    User->>Gateway: 发送请求
    Gateway->>AgentCmd: agentCommandFromIngress
    
    AgentCmd->>AgentCmd: prepareAgentCommandExecution
    AgentCmd->>Queue: enqueueSession/enqueueGlobal
    
    alt 队列有空位
        Queue-->>AgentCmd: 允许执行
        AgentCmd->>Model: runWithModelFallback
        
        loop 事件驱动循环
            Model->>Session: 创建Agent Session
            Session->>Session: subscribeEmbeddedPiSession
            
            par 流式事件处理
                Session-->>User: lifecycle事件(start)
                Session-->>User: assistant增量文本流
                Session-->>User: tool_start事件
            end
            
            Session->>Tools: 调用工具
            
            alt 工具执行成功
                Tools-->>Session: tool_delta/tool_end
                Session-->>User: 工具结果
            else 工具执行失败
                Tools-->>Session: 错误事件
                Session-->>User: 错误信息
            end
            
            Session->>Context: 检查上下文窗口
            
            alt 上下文溢出
                Context->>Context: compact()压缩
                Note over Session,Model: 触发重试(最多160次)
                Session->>Model: 重新推理
            else 正常结束
                Session-->>User: lifecycle(end)
            end
        end
        
        Session->>Session: 持久化Transcript
        Session-->>AgentCmd: 返回结果
    else 队列已满
        Queue-->>AgentCmd: 排队等待
    end
    
    AgentCmd-->>Gateway: 返回响应
    Gateway-->>User: 最终结果 -->
![](https://cdn.nlark.com/yuque/__mermaid_v3/90094e6cf8ba2a92e64ff3786c4efa04.svg)

## 三、模块依赖关系图
<!-- 这是一个文本绘图，源码为：graph LR
    subgraph "入口模块"
        Entry[entry/index]
    end
    
    subgraph "网关模块"
        Gateway[gateway]
        CLI[cli]
        TUI[tui]
    end
    
    subgraph "核心模块"
        Agents[agents]
        Context[context-engine]
        Sessions[sessions]
        Plugins[plugins]
    end
    
    subgraph "工具模块"
        Browser[browser]
        ImageGen[image-generation]
        WebSearch[web-search]
        Process[process]
    end
    
    subgraph "集成模块"
        Channels[channels]
        AutoReply[auto-reply]
        Cron[cron]
    end
    
    subgraph "基础模块"
        Config[config]
        Providers[providers]
        Security[security]
        Logging[logging]
    end
    
    %% 依赖关系
    Entry --> Gateway
    Entry --> CLI
    Entry --> TUI
    
    Gateway --> Agents
    CLI --> Agents
    TUI --> Agents
    
    Agents --> Plugins
    Agents --> Context
    Agents --> Sessions
    
    Agents --> Browser
    Agents --> ImageGen
    Agents --> WebSearch
    Agents --> Process
    
    Agents --> Channels
    Agents --> AutoReply
    Agents --> Cron
    
    Agents --> Config
    Agents --> Providers
    Agents --> Security
    Agents --> Logging
    
    Sessions --> Config
    Providers --> Config
    Channels --> Security -->
![](https://cdn.nlark.com/yuque/__mermaid_v3/37cfb0b61e77eb42a1c45f4030679aae.svg)

## 四、工具调用架构图
<!-- 这是一个文本绘图，源码为：graph TB
    subgraph "工具创建入口"
        CreateTools[createOpenClawCodingTools<br/>src/agents/pi-tools.ts]
    end

    subgraph "工具来源"
        BaseTools["基础Coding工具<br/>@mariozechner/pi-coding-agent<br/>read/write/edit/bash/apply_patch"]
        
        CustomTools["自定义工具<br/>src/agents/openclaw-tools.ts<br/>browser/canvas/cron/gateway/message/tts<br/>web_search/web_fetch/image/image_generate/pdf<br/>sessions_*/agents_list/subagents/nodes"]
        
        PluginTools["插件工具<br/>src/plugins/tools.ts<br/>resolvePluginTools动态加载"]
    end

    subgraph "工具策略控制"
        Policy[Tool Policy Pipeline]
        Sandbox[沙箱环境限制]
        Subagent[子Agent权限隔离]
    end

    subgraph "工具执行钩子"
        BeforeHook[before_tool_call钩子<br/>src/agents/pi-tools.before-tool-call.ts]
        LoopDetect[循环检测<br/>detectToolCallLoop]
        ResultHandler[工具结果处理<br/>emitToolResultMessage]
    end

    CreateTools --> BaseTools
    CreateTools --> CustomTools
    CreateTools --> PluginTools
    
    BaseTools --> Policy
    CustomTools --> Policy
    PluginTools --> Policy
    
    Policy --> Sandbox
    Policy --> Subagent
    
    Sandbox --> BeforeHook
    Subagent --> BeforeHook
    
    BeforeHook --> LoopDetect
    LoopDetect --> ResultHandler -->
![](https://cdn.nlark.com/yuque/__mermaid_v3/b663ee4dc7eacc689c5884a94b981fc9.svg)

## 五、数据流全景图
<!-- 这是一个文本绘图，源码为：flowchart TD
    Start([用户请求]) --> Validate[参数验证]
    Validate --> ModelSelect[模型选择]
    ModelSelect --> QueueWait[队列等待]
    
    QueueWait --> Workspace[工作区准备]
    Workspace --> Prompt[System Prompt构建]
    Prompt --> Session[创建Agent Session]
    
    subgraph EventLoop [事件循环]
        direction TB
        Infer[模型推理] --> ToolCall{是否需要工具?}
        ToolCall -->|是| Execute[执行工具]
        Execute --> CheckOverflow{上下文溢出?}
        CheckOverflow -->|是| Compact[上下文压缩]
        Compact --> Infer
        CheckOverflow -->|否| Infer
        ToolCall -->|否| End[结束循环]
    end
    
    Session --> EventLoop
    EventLoop --> Aggregate[结果聚合]
    Aggregate --> Persist[Transcript持久化]
    Persist --> Response[返回结果]
    
    style EventLoop fill:#f9f,stroke:#333,stroke-width:2px
    style Compact fill:#ff9,stroke:#333
    style ToolCall fill:#9ff,stroke:#333 -->
![](https://cdn.nlark.com/yuque/__mermaid_v3/3240cb6972d215f38c55a8a6499608a2.svg)

## 六、部署架构图
<!-- 这是一个文本绘图，源码为：graph TB
    subgraph "客户端"
        Browser[浏览器]
        Terminal[终端]
        API[API客户端]
    end

    subgraph "负载均衡层"
        LB[负载均衡器]
    end

    subgraph "应用服务器集群"
        App1[OpenClaw实例1]
        App2[OpenClaw实例2]
        App3[OpenClaw实例N]
    end

    subgraph "基础设施"
        Redis[(Redis<br/>队列/缓存)]
        DB[(PostgreSQL<br/>会话/Transcript)]
        S3[(对象存储<br/>文件/图像)]
    end

    subgraph "外部服务"
        OpenAI[OpenAI API]
        Anthropic[Anthropic API]
        Google[Google AI]
        Playwright[Playwright浏览器]
    end

    Browser --> LB
    Terminal --> LB
    API --> LB
    
    LB --> App1
    LB --> App2
    LB --> App3
    
    App1 --> Redis
    App2 --> Redis
    App3 --> Redis
    
    App1 --> DB
    App2 --> DB
    App3 --> DB
    
    App1 --> S3
    App2 --> S3
    App3 --> S3
    
    App1 --> OpenAI
    App1 --> Anthropic
    App1 --> Google
    App1 --> Playwright -->
![](https://cdn.nlark.com/yuque/__mermaid_v3/a2eba50b160d58b416dc013a07970794.svg)

## 七、核心组件关系矩阵
| 组件 | 职责 | 依赖 | 被依赖 | 关键文件 |
| --- | --- | --- | --- | --- |
| **Gateway** | RPC入口 | Agents | CLI/TUI | server-methods/agent.ts |
| **AgentCommand** | 命令处理 | Queue, Model | Gateway | agent-command.ts |
| **PiAgentCore** | Agent循环 | Tools, Context | AgentCommand | node_modules/pi-agent-core |
| **SessionManager** | 会话控制 | Storage | Agents | sessions/index.ts |
| **ContextEngine** | 上下文压缩 | - | Agents | context-engine/compact.ts |
| **PluginSystem** | 钩子扩展 | - | Agents | plugins/hooks.ts |
| **ToolExecutor** | 工具执行 | Tools | PiAgentCore | pi-tools.before-tool-call.ts |
| **ModelSelector** | 模型选择 | Providers | Agents | model-selection.ts |


---

**架构特点总结：**

1. **分层清晰**：用户接入层、核心处理层、工具层、基础设施层职责分明
2. **事件驱动**：基于流式事件而非传统的ReAct模式
3. **高扩展性**：插件系统+钩子机制，支持功能扩展
4. **容错性强**：模型回退、上下文压缩、重试机制保障稳定性
5. **并发控制**：Session Lane队列确保串行执行
6. **模块解耦**：各模块通过明确定义的接口交互




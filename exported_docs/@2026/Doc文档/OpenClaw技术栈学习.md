# OpenClaw 技术栈深度分析
## 一、核心语言与运行时
| 类别 | 技术 | 细节 |
| --- | --- | --- |
| **主语言** | TypeScript | 项目核心代码全部使用 TypeScript，strict: true，target: ES2023，module: NodeNext |
| **运行时** | Node.js ≥ 22.16.0 | 要求 Node.js 22+，Docker 镜像使用 node:24-bookworm |
| **构建工具** | tsdown | 用于构建 TypeScript 项目为单文件输出 |
| **打包工具** | pnpm 10.23.0 | monorepo 包管理器，pnpm-workspace.yaml 管理多工作空间 |
| **执行器** | tsx | 开发/脚本阶段运行 TypeScript |
| **格式化** | oxfmt 0.40.0 | 代码格式化工具（替代 Prettier） |
| **Linter** | oxlint 1.55.0 | TypeScript ESLint 替代品，支持类型感知检查 |
| **Python** | pytest + ruff | 仅用于 skills 目录的测试，pyproject.toml 配置 |


---

## 二、核心框架与库
### 2.1 AI / LLM 集成
| 库 | 用途 |
| --- | --- |
| @agentclientprotocol/sdk 0.16.1 | Agent Client Protocol (ACP) 协议 SDK |
| @mariozechner/pi-agent-core 0.58.0 | 核心 AI Agent 运行时 |
| @mariozechner/pi-ai 0.58.0 | AI 模型集成 |
| @mariozechner/pi-coding-agent 0.58.0 | 编程类 Agent |
| @mariozechner/pi-tui 0.58.0 | TUI 界面 |
| @modelcontextprotocol/sdk 1.27.1 | MCP (Model Context Protocol) SDK |
| hono 4.12.7 | 轻量级 Web 框架，用于 HTTP 服务 |
| express 5.2.1 | HTTP 服务器（部分模块使用） |


### 2.2 消息/通信通道
| 库 | 用途 |
| --- | --- |
| grammy 1.41.1 | Telegram Bot 框架 |
| @grammyjs/runner 2.0.3 | Telegram 轮询运行器 |
| @grammyjs/transformer-throttler 1.2.1 | Telegram 节流 |
| @slack/bolt 4.6.0 | Slack Bot 框架 |
| @discordjs/voice 0.19.1 | Discord 语音支持 |
| discord-api-types 0.38.42 | Discord 类型定义 |
| @line/bot-sdk 10.6.0 | LINE Messaging API |
| @larksuiteoapi/node-sdk 1.59.0 | 飞书 (Feishu) SDK |
| @whiskeysockets/baileys 7.0.0-rc.9 | WhatsApp Baileys 协议 |
| @matrix-org/matrix-sdk-crypto-nodejs | Matrix 加密（仅构建依赖） |


### 2.3 数据与存储
| 库 | 用途 |
| --- | --- |
| @lancedb/lancedb 0.26.2 | 向量数据库 (LanceDB) |
| sqlite-vec 0.1.7-alpha.2 | SQLite 向量扩展 |
| jszip 3.10.1 | ZIP 文件处理 |
| json5 2.2.3 | JSON5 解析 |


### 2.4 媒体处理
| 库 | 用途 |
| --- | --- |
| sharp 0.34.5 | 图像处理（仅构建依赖） |
| pdfjs-dist 5.5.207 | PDF.js 用于 PDF 渲染 |
| @napi-rs/canvas | Canvas 渲染（peer dependency） |
| @mozilla/readability 0.6.0 | 文章内容提取 |
| @discordjs/voice + opusscript | 语音编码 |
| node-edge-tts 1.2.10 | 微软 Edge TTS 语音合成 |


### 2.5 基础设施
| 库 | 用途 |
| --- | --- |
| @aws-sdk/client-bedrock 3.1009.0 | AWS Bedrock AI 服务 |
| @sinclair/typebox 0.34.48 | JSON Schema 类型系统 |
| zod 4.3.6 | 运行时 schema 验证 |
| ajv 8.18.0 | JSON Schema 验证 |
| yaml 2.8.2 | YAML 解析 |
| dotenv 17.3.1 | 环境变量 |
| undici 7.24.1 | HTTP 客户端（Node.js 内置 fetch 替代） |
| ws 8.19.0 | WebSocket 服务 |
| chokidar 5.0.0 | 文件监听 |
| tar 7.5.11 | 压缩包处理 |
| file-type 21.3.2 | 文件类型检测 |
| @buape/carbon 0.0.0-beta-20260216184201 | 内部 UI 框架 |
| croner 10.0.1 | Cron 定时任务 |
| long 5.3.2 | 长整数处理（Protocol Buffers 兼容） |
| jiti 2.6.1 | TypeScript/ESM 即时转译 |
| commander 14.0.3 | CLI 命令行框架 |
| @clack/prompts 1.1.0 | 交互式 CLI 提示 |
| tslog 4.10.2 | 日志库 |
| cli-highlight 2.1.11 | CLI 高亮输出 |
| @homebridge/ciao 1.3.5 | mDNS/NSD 服务发现 |


### 2.6 测试
| 库 | 用途 |
| --- | --- |
| vitest 4.1.0 | 单元/集成测试框架 |
| @vitest/coverage-v8 4.1.0 | V8 覆盖率 |
| jsdom 28.1.0 | DOM 模拟 |
| playwright 1.58.2 | E2E 测试 |
| @vitest/browser-playwright 4.1.0 | Vitest + Playwright 集成 |
| playwright-core 1.58.2 | Playwright 核心库 |
| jscpd 4.0.8 | 代码重复检测 |
| knip | 死代码检测 |


---

## 三、架构层分析
### 3.1 Monorepo 结构（pnpm workspaces）
```plain
openclaw/
├── packages/         # 兼容桥接包
│   ├── clawdbot/     # clawdbot → openclaw 桥接
│   └── moltbot/      # moltbot → openclaw 桥接
├── packages/*/       # 大量私有包
├── ui/               # 控制面板 (Control UI)
├── src/              # 核心源码
│   ├── gateway/      # 网关服务
│   ├── cli/          # 命令行入口
│   ├── tui/          # 终端 UI
│   ├── channels/     # 通道层
│   ├── plugins/      # 插件系统
│   ├── providers/    # AI 模型提供者
│   ├── runtime/      # 运行时
│   ├── acp/          # ACP 协议
│   └── ...
├── extensions/       # 扩展模块
│   ├── channel-*/    # 渠道插件 (telegram, discord, slack, ...)
│   ├── provider-*/   # 模型提供者 (anthropic, openai, ollama, ...)
│   ├── memory-*/     # 记忆存储 (memory-core, memory-lancedb)
│   └── ...
└── apps/             # 原生应用
    ├── android/      # Android (Kotlin + Jetpack Compose)
    ├── ios/          # iOS (Swift + SwiftUI)
    └── macos/        # macOS (Swift + AppKit/SwiftUI)
```

### 3.2 核心架构分层
```plain
┌─────────────────────────────────────────┐
│         CLI / TUI / Control UI          │  入口层
├─────────────────────────────────────────┤
│               Gateway                   │  网关层
├─────────────────────────────────────────┤
│         ACP Protocol Layer              │  协议层
├─────────────────────────────────────────┤
│        Channel / Plugin Layer           │  通道/插件层
│   (telegram, discord, slack, matrix...) │
├─────────────────────────────────────────┤
│        Provider / LLM Layer             │  AI 模型层
│  (anthropic, openai, ollama, bedrock...)│
├─────────────────────────────────────────┤
│        Runtime / Memory Layer           │  运行时/记忆层
│      (lancedb, sqlite-vec, mcp)         │
└─────────────────────────────────────────┘
```

---

## 四、原生应用技术栈
### 4.1 Android
+ **语言**: Kotlin 2.2.21
+ **构建**: Gradle 9.0.1 + Android Gradle Plugin 9.0.1
+ **UI**: Jetpack Compose (Kotlin Plugin Compose)
+ **序列化**: Kotlin Serialization Plugin 2.2.21
+ **代码风格**: ktlint 14.0.1
+ **编译 SDK**: Android API 36

### 4.2 iOS
+ **语言**: Swift
+ **构建**: XcodeGen (project.yml)
+ **框架**: SwiftUI / AppKit
+ **Watch**: WatchOS 应用支持
+ **Share Extension**: iOS 分享扩展

### 4.3 macOS
+ **语言**: Swift
+ **框架**: AppKit
+ **组件**: OpenClawKit, OpenClawProtocol, OpenClawIPC, OpenClawDiscovery

---

## 五、部署与基础设施
### 5.1 容器化
+ **Docker**: 多阶段构建，bookworm (Debian 12) 基础镜像
+ **Podman**: 兼容 Docker 的容器运行时
+ **docker-compose**: 开发/测试环境编排
+ **支持按需编译** native 模块（node-llama-cpp, sharp, node-pty 等）

### 5.2 部署平台
+ **Fly.io**: fly.toml 配置
+ **Render**: render.yaml 配置
+ **Homebrew**: macOS 安装支持
+ **appcast.xml**: macOS 自动更新 (Sparkle 框架)

---

## 六、扩展系统（Extensions）
项目包含 **60+ 扩展模块**，分为三大类：

### 6.1 消息渠道 (20+)
Telegram, Discord, Slack, WhatsApp, LINE, iMessage (BlueBubbles), Matrix, Signal, IRC, Mattermost, Microsoft Teams, Google Chat, Feishu, Synology Chat, Nostr, Twitch, Nextcloud Talk, Zalo, X (Twitter DMs), iPhone Voice Call

### 6.2 AI 模型提供者 (20+)
Anthropic, OpenAI, Google (Gemini), AWS Bedrock, Ollama, OpenRouter, Groq, Mistral, HuggingFace, Together AI, Perplexity, Firecrawl, Vercel AI Gateway, Cloudflare AI Gateway, Volcengine, Minimax, Moonshot, Kimi, Qwen, NVIDIA NIM, SGLang, vLLm, XAI, Brave Search, OpenCode, OpenShell 等

### 6.3 核心能力扩展
+ **记忆系统**: memory-core, memory-lancedb (向量数据库)
+ **设备配对**: device-pair (设备配对授权)
+ **代码执行**: llm-task, synthetic, open-prose
+ **诊断**: diagnostics-otel (OpenTelemetry)
+ **TTS/语音**: elevenlabs, talk-voice, voice-call
+ **安全**: thread-ownership, allowlist-config-edit

---

## 七、插件 SDK
`openclaw/plugin-sdk` 是核心插件开发接口，提供以下子模块：

| SDK 模块 | 功能 |
| --- | --- |
| setup | 插件安装向导 |
| provider-setup | 模型提供者配置 |
| channel-runtime | 渠道运行时 |
| agent-runtime | Agent 运行时 |
| gateway-runtime | 网关运行时 |
| cli-runtime | CLI 运行时 |
| security-runtime | 安全策略 |
| media-runtime | 媒体处理 |
| speech-runtime | 语音处理 |
| conversation-runtime | 对话管理 |
| reply-runtime | 回复生成 |
| sandbox | 沙箱隔离 |
| acp-runtime | ACP 协议运行时 |


---

## 八、关键技术特性
| 特性 | 描述 |
| --- | --- |
| **多协议支持** | ACP (Agent Client Protocol) + MCP (Model Context Protocol) |
| **多渠道聚合** | 统一处理来自 20+ 消息平台的会话 |
| **多模型路由** | 支持 20+ AI 模型提供者的智能路由 |
| **向量记忆** | LanceDB + SQLite-Vec 实现语义记忆检索 |
| **沙箱执行** | Docker 隔离的代码执行环境 |
| **跨平台** | Node.js (Linux/macOS/Windows) + Android + iOS + macOS |
| **类型安全** | 全链路 TypeScript strict 模式 + Zod 运行时验证 + TypeBox JSON Schema |
| **热更新** | 插件动态加载，代码热重载 |


---

## 九、总结
**OpenClaw** 是一个**企业级的 AI 网关平台**，基于 **TypeScript + Node.js** 构建，支持：

+ **多渠道消息聚合**（20+ 消息平台）
+ **多 AI 模型接入**（20+ 模型提供商）
+ **跨平台部署**（服务器端 + 移动端 + 桌面端）

其核心设计理念是通过**插件化的扩展系统**连接各种消息渠道和 AI 模型，为用户和 AI Agent 之间提供**统一的通信桥梁**。





# OpenClaw 项目微服务拆分可行性分析报告
## 一、项目架构总结
OpenClaw 是一个**高度模块化的多渠道 AI 网关平台**，当前架构为**单体 + 插件化**设计：

+ **技术栈**: TypeScript (Node.js 22+) + pnpm monorepo
+ **核心协议**: ACP (Agent Communication Protocol) + WebSocket/HTTP
+ **存储**: 无外部数据库，纯文件系统 (SQLite JSON 文件 + LanceDB 向量)
+ **构建**: tsdown + Vite
+ **部署**: Docker (多阶段构建)、Fly.io、Render.com、systemd/launchd
+ **包结构**: pnpm workspaces (根包 + packages + extensions + apps + ui)
+ **扩展数量**: 90+ 插件扩展（40+ AI Provider、40+ 消息渠道）

### 请求处理流程
```plain
用户请求 (多渠道: Telegram/Discord/Slack/WhatsApp/...)
      │
      ▼
Gateway HTTP/WebSocket 接入层
      │ (认证/限流/CSP)
      ▼
消息路由层 (routing/resolve-route.ts)
      ├──► 渠道管理层 (channels/)
      │         └──► 40+ 渠道插件 (extensions/)
      │
      └──► Agent 执行层 (agents/)
                ├──► PI Runner / 子Agent管理
                ├──► AI Provider层 (providers/)
                │         └──► 40+ LLM (Anthropic/OpenAI/Ollama/Gemini...)
                ├──► 插件工具层 (plugins/runtime/)
                ├──► 向量记忆层 (memory/)
                ├──► 浏览器控制 (browser/)
                └──► 沙箱执行 (sandbox/)
```

---

## 二、微服务拆分可行性评估
### 2.1 当前架构的微服务友好特性
| 特性 | 现状 | 微服务友好度 |
| --- | --- | --- |
| 模块边界清晰 | routing/channels/agents/providers/plugins 层次分明 | ✅ 优秀 |
| 插件系统 | 90+ 独立插件可通过接口扩展 | ✅ 优秀 |
| 协议定义 | ACP 协议已定义跨服务通信 schema | ✅ 优秀 |
| 配置驱动 | JSON5 配置声明式管理渠道/Provider/Agent | ✅ 优秀 |
| 无数据库依赖 | 纯文件系统，无需数据迁移 | ✅ 有利 |
| 多客户端 | 支持 Web/iOS/Android/macOS 多端接入 | ✅ 有利 |
| 已有远程节点架构 | NodeRegistry + Remote Nodes 模式 | ✅ 优秀 |
| Docker 支持 | 已有 Dockerfile/docker-compose | ✅ 优秀 |


### 2.2 当前架构的微服务挑战
| 挑战 | 严重程度 | 说明 |
| --- | --- | --- |
| 共享配置 | 🔴 高 | 所有模块共享 ~/.openclaw/config.json5，拆分后需独立配置中心 |
| 单进程事件总线 | 🟡 中 | agent-events.ts、heartbeat-events.ts 等事件在进程内传递 |
| 插件运行时紧耦合 | 🟡 中 | PluginRuntime 依赖注入与主进程深度绑定 |
| Session 存储 | 🟡 中 | config/sessions.ts 的 SQLite 会话与配置紧耦合 |
| 无消息队列 | 🟡 中 | 当前无异步消息队列（MQ），服务间通信依赖直接调用 |
| 向量存储 | 🟡 中 | LanceDB 嵌入在主进程中，拆分需独立向量服务 |
| 安全审计 | 🟡 中 | security/audit.ts 审计日志在主进程内写入 |


### 2.3 综合评估
**结论**: 可以进行微服务拆分，但建议采用**渐进式拆分策略**，而非一次性全部拆分。

**理由**:

1. 项目架构分层清晰，模块边界明确，具备微服务拆分的基础
2. ACP 协议已为跨服务通信打下基础
3. 但当前无消息队列基础设施，直接 HTTP 调用会导致同步耦合
4. 建议优先拆分**独立性强、变更频率低、对延迟不敏感**的模块

---

## 三、推荐的微服务拆分方案
### 方案一：渐进式拆分（推荐——风险最低）
保留当前单体架构，逐步将独立模块以 **Sidecar 模式** 或 **独立进程模式** 拆分：

```plain
┌─────────────────────────────────────────────────────┐
│                  Gateway (主进程)                    │
│  HTTP/WebSocket / 认证 / 限流 / 路由 / 事件总线      │
└─────────────────────────────────────────────────────┘
          │                    │                    │
          ▼                    ▼                    ▼
┌───────────────┐  ┌─────────────────┐  ┌──────────────────┐
│ Channel       │  │ AI Provider     │  │ Memory           │
│ Gateway       │  │ Gateway         │  │ Service          │
│ (渠道代理服务) │  │ (AI路由网关)    │  │ (向量记忆服务)    │
└───────────────┘  └─────────────────┘  └──────────────────┘
          │                    │                    │
          ▼                    ▼                    ▼
     40+ 渠道插件        40+ LLM Provider     LanceDB/SQLite
     (独立进程/容器)      (API代理+缓存)       (独立存储)
```

### 方案二：领域驱动拆分（完全微服务化）
基于 DDD 领域划分，拆分为以下微服务架构：

```plain
                      ┌─────────────────────────────────────────┐
                      │            Client Layer                  │
                      │  (Web / iOS / Android / macOS / CLI)    │
                      └─────────────────┬───────────────────────┘
                                        │ WebSocket + HTTPS
                                        ▼
                      ┌─────────────────────────────────────────┐
                      │         API Gateway (BFF Layer)          │
                      │  (Gateway Service - 认证/限流/路由)      │
                      └─────────────────┬───────────────────────┘
                                        │ ACP over HTTP/WS
              ┌─────────────────────────┼─────────────────────────┐
              │                         │                         │
              ▼                         ▼                         ▼
┌───────────────────┐    ┌─────────────────────┐    ┌────────────────────┐
│ Channel Gateway   │    │  Agent Execution   │    │  AI Provider       │
│ Service           │    │  Service           │    │  Gateway           │
│ (40+ 渠道管理)     │    │  (PI Runner/Sandbox)│    │  (40+ LLM 聚合)    │
└───────────────────┘    └─────────────────────┘    └────────────────────┘
              │                         │                         │
              └─────────────────────────┼─────────────────────────┘
                                        │
                      ┌─────────────────┴───────────────────────┐
                      │         Shared Infrastructure            │
                      │  (RabbitMQ / Redis / PostgreSQL)         │
                      └─────────────────┬───────────────────────┘
                                        │
              ┌─────────────────────────┼─────────────────────────┐
              │                         │                         │
              ▼                         ▼                         ▼
┌───────────────────┐    ┌─────────────────────┐    ┌────────────────────┐
│  Memory Service   │    │  Config Service     │    │  Security Service  │
│  (向量记忆)        │    │  (配置管理)          │    │  (审计日志)         │
└───────────────────┘    └─────────────────────┘    └────────────────────┘
```

---

## 四、推荐拆分的微服务清单
### 4.1 核心服务（必须保留在主进程或最早拆分）
#### 🔵 Gateway Service —— 网关核心服务
| 项目 | 内容 |
| --- | --- |
| **职责** | HTTP/WebSocket 接入、认证鉴权、限流、消息路由 |
| **核心文件** | src/gateway/server-http.ts, server-chat.ts, auth.ts |
| **保留理由** | 网关核心，与所有模块强关联，最不适合拆分 |
| **建议** | 作为 BFF (Backend-For-Frontend) 层，代理到其他微服务 |


### 4.2 可独立拆分的微服务
#### 🟢 Service 1: Channel Gateway Service —— 渠道网关服务
| 项目 | 内容 |
| --- | --- |
| **职责** | 管理所有消息渠道的连接生命周期、消息收发、渠道特定的协议处理 |
| **核心文件** | src/channels/, src/gateway/server-channels.ts, extensions/*/ |
| **可拆分理由** | ✅ 渠道是 IO 密集型，与 CPU 计算型 Agent 执行解耦   ✅ 40+ 渠道插件独立加载，互不干扰   ✅ 渠道协议差异大，需要独立管理   ✅ 渠道故障不应影响 Agent 执行 |
| **拆分后接口** | POST /channels/connect → 连接渠道   POST /channels/disconnect → 断开渠道   POST /channels/send → 发送消息   WS /channels/events → 渠道事件流   GET /channels/status → 渠道健康状态 |
| **数据依赖** | 渠道配置 (config.json5 channels.*)、渠道会话状态 (SQLite) |
| **独立部署** | 每个渠道类型可独立 Docker 容器 |


#### 🟢 Service 2: Agent Execution Service —— Agent 执行服务
| 项目 | 内容 |
| --- | --- |
| **职责** | PI Runner 管理、子 Agent 生命周期、代码执行沙箱、Skills 管理 |
| **核心文件** | src/agents/subagent-registry.ts, src/agents/pi-embedded-runner/, src/agents/sandbox/, src/browser/ |
| **可拆分理由** | ✅ CPU 密集型，与 IO 密集型的渠道层自然解耦   ✅ 沙箱执行需要独立资源隔离   ✅ 子 Agent 管理有独立的生命周期   ✅ Skills 加载和刷新可独立进行 |
| **拆分后接口** | POST /agent/run → 触发 Agent 执行   GET /agent/run/{id}/status → 执行状态   WS /agent/run/{id}/stream → 流式输出   POST /agent/skill/refresh → 刷新 Skills   POST /agent/sandbox/spawn → 启动沙箱 |
| **数据依赖** | Agent 配置 (config.json5 agents._)、Skills 定义 (skills/_.md)、工作区文件、沙箱状态 |


#### 🟢 Service 3: AI Provider Gateway —— AI 路由网关
| 项目 | 内容 |
| --- | --- |
| **职责** | 统一管理 40+ AI Provider 的连接、模型选择、降级策略、Token 计数、计费 |
| **核心文件** | src/providers/, src/providers/model-catalog.ts, src/providers/model-fallback.ts |
| **可拆分理由** | ✅ Provider 数量多，需要专门维护   ✅ 模型降级、Token 计数等逻辑复杂   ✅ API Key 管理需要高安全级别   ✅ 多 Provider 聚合、负载均衡需要独立服务   ✅ 新增 Provider 不应影响其他服务 |
| **拆分后接口** | POST /ai/chat → 统一聊天接口   POST /ai/embed → 向量嵌入   GET /ai/models → 可用模型列表   POST /ai/token/count → Token 计数   GET /ai/usage/{account} → 用量统计 |
| **独立部署** | 无状态，可水平扩展，多实例负载均衡 |


#### 🟢 Service 4: Memory Service —— 记忆/向量服务
| 项目 | 内容 |
| --- | --- |
| **职责** | Agent 记忆存储、向量搜索、RAG 上下文注入 |
| **核心文件** | src/memory/, src/memory/vector-index.ts, extensions/memory-lancedb/ |
| **可拆分理由** | ✅ 向量数据库 LanceDB 可以独立部署   ✅ RAG 上下文注入是独立的检索流程   ✅ 记忆持久化需求与主服务不同   ✅ 可独立扩展向量索引规模 |
| **拆分后接口** | POST /memory/add → 添加记忆   POST /memory/search → 向量相似搜索   POST /memory/recall → 上下文召回   POST /memory/delete → 删除记忆   GET /memory/stats → 记忆统计 |
| **独立部署** | LanceDB 可独立容器，或使用云向量服务 |


#### 🟢 Service 5: Config Management Service —— 配置管理服务
| 项目 | 内容 |
| --- | --- |
| **职责** | 配置的加载、验证、迁移、热重载、版本管理 |
| **核心文件** | src/config/config.ts, src/config/zod-schema.ts, src/config/sessions.ts |
| **可拆分理由** | ✅ 配置管理是基础设施服务，所有其他服务都需要   ✅ 配置变更需要广播到所有服务   ✅ 配置迁移逻辑复杂，独立后易于维护   ✅ 可实现配置版本化和回滚 |
| **拆分后接口** | GET /config → 获取完整配置   PUT /config → 更新配置   POST /config/validate → 验证配置   GET /config/snapshot → 配置快照   POST /config/migrate → 执行迁移   WS /config/watch → 配置变更订阅 |
| **依赖** | PostgreSQL (推荐，用于配置版本化) 或 etcd/consul |


#### 🟢 Service 6: Session & State Service —— 会话状态服务
| 项目 | 内容 |
| --- | --- |
| **职责** | 会话管理、消息历史、状态持久化、定时任务（Cron） |
| **核心文件** | src/config/sessions.ts, src/gateway/server-cron.ts, src/auto-reply/ |
| **可拆分理由** | ✅ 会话状态与其他业务逻辑解耦   ✅ Cron 定时任务独立后更易于调度管理   ✅ 消息历史的分页、搜索、归档需要专门优化   ✅ 可支持会话状态的多副本同步 |
| **拆分后接口** | GET /session/{key} → 获取会话   POST /session → 创建会话   PUT /session/{key} → 更新会话   GET /session/{key}/messages → 消息历史   POST /cron/schedule → 创建定时任务   GET /cron/jobs → 定时任务列表 |
| **依赖** | PostgreSQL (会话+消息) + Redis (会话缓存) + SQLite (Cron持久化) |


#### 🟢 Service 7: Security & Audit Service —— 安全审计服务
| 项目 | 内容 |
| --- | --- |
| **职责** | 安全策略执行、审计日志、工具策略、DM 策略、外部内容检测 |
| **核心文件** | src/security/audit.ts, src/security/path-policy.ts, src/security/tool-policy.ts |
| **可拆分理由** | ✅ 安全策略是横切关注点，独立后便于统一管理   ✅ 审计日志需要高可靠写入，不应被业务服务阻塞   ✅ 安全策略变更应实时生效且不影响业务   ✅ 可对接 SIEM 系统 |
| **拆分后接口** | POST /security/audit → 记录审计事件   GET /security/policy → 获取安全策略   POST /security/check → 安全检查   GET /security/alerts → 安全告警 |
| **依赖** | PostgreSQL (审计日志) 或 Elasticsearch (日志聚合) |


#### 🟢 Service 8: Media Processing Service —— 媒体处理服务
| 项目 | 内容 |
| --- | --- |
| **职责** | 图片处理、PDF 解析、语音合成 (TTS)、图像生成 |
| **核心文件** | src/media/, src/image-generation/, src/tts/ |
| **可拆分理由** | ✅ 媒体处理是 CPU/内存密集型，独立后资源隔离   ✅ 图片处理库依赖系统库，独立部署更简单   ✅ TTS/图像生成可对接外部服务，独立后易于切换   ✅ 媒体处理失败不应影响核心聊天流程 |
| **拆分后接口** | POST /media/process → 媒体处理   POST /media/thumbnail → 生成缩略图   POST /media/ocr → OCR 识别   POST /tts/synthesize → 语音合成   POST /image/generate → 图像生成 |
| **独立部署** | 需要较高内存，可使用独立 GPU 资源 |


### 4.3 服务间通信架构
```plain
                           ┌──────────────────────────────────┐
                           │        Service Mesh Layer          │
                           │  (推荐: 内部用 HTTP/gRPC + MQ)    │
                           └──────────────────────────────────┘
                                          │
      ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
      │  Channel    │    │   Agent     │    │     AI      │    │   Memory    │
      │  Gateway    │    │  Execution  │    │  Provider   │    │   Service   │
      │  Service    │    │   Service   │    │  Gateway    │    │             │
      └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
             │                  │                  │                  │
             └──────────────────┴──────────────────┴──────────────────┘
                                     │
                           ┌─────────────────┐
                           │  Config/Session │
                           │    Service      │
                           └─────────────────┘
```

**推荐通信模式**:

+ **同步调用**: HTTP REST 或 gRPC（用于实时请求/响应）
+ **异步事件**: Redis Pub/Sub 或 RabbitMQ/Kafka（用于事件通知）
+ **服务发现**: Consul / etcd / Kubernetes DNS

### 4.4 数据存储分离方案
| 服务 | 推荐存储 | 说明 |
| --- | --- | --- |
| Gateway | SQLite (当前) | 保持简单 |
| Config Service | PostgreSQL | 配置版本化、多租户 |
| Session Service | PostgreSQL + Redis | 消息历史+会话缓存 |
| Memory Service | LanceDB + PostgreSQL | 向量+结构化记忆 |
| AI Provider Gateway | PostgreSQL | Token 用量计费 |
| Security Service | PostgreSQL + Elasticsearch | 审计日志聚合 |
| Media Service | S3/MinIO + Redis | 媒体文件存储 |


---

## 五、拆分优先级和风险评估
### 5.1 优先级排序
| 阶段 | 服务 | 难度 | 理由 |
| --- | --- | --- | --- |
| **第一阶段** | Media Processing Service | 低 | 最独立，无状态 |
|  | AI Provider Gateway | 低 | 无状态，可灰度 |
|  | Security & Audit Service | 低 | 旁路服务，不阻塞主流程 |
| **第二阶段** | Memory Service | 中 | 向量库独立部署 |
|  | Channel Gateway Service | 中 | 渠道解耦，但协议复杂 |
| **第三阶段** | Agent Execution Service | 高 | 沙箱、Skills 依赖多 |
|  | Config Management Service | 高 | 牵一发动全身 |
|  | Session & State Service | 高 | 会话状态迁移成本高 |


### 5.2 关键风险
| 风险 | 影响 | 缓解措施 |
| --- | --- | --- |
| 服务间延迟增加 | WebSocket 消息路由延迟 | 同一数据中心部署、本地缓存 |
| 数据一致性 | 配置/会话跨服务同步 | 事件溯源 (Event Sourcing) |
| 部署复杂度 | 8+ 服务的运维挑战 | Kubernetes/docker-compose |
| 调试难度 | 分布式追踪需求 | 引入 OpenTelemetry + Jaeger |
| 配置迁移 | 历史配置格式兼容 | 渐进式迁移，保留迁移脚本 |


---

## 六、总结与建议
### 6.1 核心结论
1. **当前项目具备微服务拆分的技术基础**，架构分层清晰、模块边界明确、协议已定义
2. 建议采用**渐进式拆分策略**，不要一次性全部拆分，避免业务中断
3. 优先拆分**无状态/旁路服务**（AI Provider Gateway、Media Service、Security Service），积累经验后再拆分核心服务
4. **必须引入消息队列基础设施**（推荐 RabbitMQ 或 Kafka）作为服务间异步通信主干

### 6.2 微服务拆分后的架构愿景
```plain
                      ┌─────────────────────────────────────────┐
                      │            Client Layer                  │
                      │  (Web / iOS / Android / macOS / CLI)    │
                      └─────────────────┬───────────────────────┘
                                        │ WebSocket + HTTPS
                                        ▼
                      ┌─────────────────────────────────────────┐
                      │         API Gateway (BFF Layer)          │
                      │  (Gateway Service - 认证/限流/路由)      │
                      └─────────────────┬───────────────────────┘
                                        │ ACP over HTTP/WS
              ┌─────────────────────────┼─────────────────────────┐
              │                         │                         │
              ▼                         ▼                         ▼
  ┌───────────────────┐    ┌─────────────────────┐    ┌────────────────────┐
  │ Channel Gateway   │    │  Agent Execution   │    │  AI Provider       │
  │ Service           │    │  Service           │    │  Gateway           │
  │ (40+ 渠道管理)     │    │  (PI Runner/Sandbox)│    │  (40+ LLM 聚合)    │
  └───────────────────┘    └─────────────────────┘    └────────────────────┘
              │                         │                         │
              └─────────────────────────┼─────────────────────────┘
                                        │
                      ┌─────────────────┴───────────────────────┐
                      │         Shared Infrastructure            │
                      │  (RabbitMQ / Redis / PostgreSQL)         │
                      └─────────────────┬───────────────────────┘
                                        │
              ┌─────────────────────────┼─────────────────────────┐
              │                         │                         │
              ▼                         ▼                         ▼
  ┌───────────────────┐    ┌─────────────────────┐    ┌────────────────────┐
  │  Memory Service   │    │  Config Service     │    │  Security Service  │
  │  (向量记忆)        │    │  (配置管理)          │    │  (审计日志)         │
  └───────────────────┘    └─────────────────────┘    └────────────────────┘
```

### 6.3 如果当前不拆分，保持单体架构的优化建议
即使当前不进行微服务拆分，项目仍然可以在单体架构下进行以下优化：

1. **模块解耦**: 强化插件接口抽象，为未来拆分做准备
2. **引入 MQ**: 预先引入 RabbitMQ/Kafka，作为服务间异步通信基础设施
3. **健康检查**: 完善各模块的健康检查接口
4. **指标采集**: 引入 OpenTelemetry，为未来的分布式追踪做准备
5. **配置中心**: 将配置从文件系统迁移到 etcd/consul，支持动态配置










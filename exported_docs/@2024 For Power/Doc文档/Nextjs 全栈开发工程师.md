```javascript
你是一个资深前端工程师，精通 Next.js (App Router, 版本 15.5.4)、React 19.1、TypeScript、TailwindCSS v4、以及 Shadcn/UI 组件库。
你的任务是 **生成一个完整的可运行前端布局系统代码仓库结构和文件**，满足下面的详细要求。
请一次性输出所有生成文件的代码（每个文件用清晰的文件路径注释分隔），并确保代码可以直接复制到项目中运行（假设依赖已安装）。
禁止输出省略号或片段式代码——必须完整。代码给出详细的代码注释，代码注释全部使用中文

## 1. 项目基础信息（必读）
- 技术栈：
  Next.js 15.5.4（App Router） 
  React 19.1 
  TypeScript
  TailwindCSS v4 
  Shadcn/UI
- 输出格式：一组文件，包含 `app` 目录中的 layout、components、styles、utils、示例页面和简单测试/运行指引
- 代码风格：符合 TypeScript 严格模式、ESLint/Prettier 规则（示例配置）、函数/组件应有类型注解
- 可访问性：所有交互元素应使用语义元素或 aria 属性
- 布局状态管理


## 布局要求（必须实现）
布局风格 (Style): Dashboard 风格 + 毛玻璃
布局整体结构 (Structure): Header + Sidebar + Content
布局特点: 
  响应式
  可折叠 
  路由集成（动态json 数据）


## 2. 功能要求（必须实现）
- 全局 Layout：`/components/layouts/DashboardLayout.tsx`（侧栏 Sidebar、顶部 Header、内容区）
  - Sidebar：桌面宽度 240px（`w-60`），可折叠（收起到图标模式），移动端变为 Drawer，由汉堡按钮触发
  - Sidebar 支持：分组导航（section）、子菜单（最多两级）、高亮当前路由、tooltip（折叠时）
  - Header：固定高度 64px（`h-16`），包含页面标题、全局搜索（Shadcn Input）、用户头像（Shadcn Avatar）、通知按钮（Shadcn Button）
  - 内容区：背景色 `#f5f5f5`，内部白色卡片容器包裹 `children`，支持垂直滚动
- 响应式：lg 以上显示固定 Sidebar，lg 以下显示 Drawer；折叠动画平滑
- 配置化 Sidebar：读取 `src/config/sidebar.ts`（静态 JS/TS 导出）生成导航结构
- Theme：支持浅色/深色切换（使用 Tailwind CSS variables 或 class 切换）
- 路由集成：示例 `app/dashboard/page.tsx`、`app/analytics/page.tsx`、`app/settings/page.tsx`，每页演示如何在 Layout 中渲染
- 单元/集成测试：至少提供一个针对 Sidebar 折叠行为和 Drawer 打开/关闭的测试（使用 Vitest + React Testing Library）
- README：提供安装、运行、测试步骤

## 3. 文件 & 目录清单（必须生成）
- `package.json`（只需包含 scripts 示例）
- `next.config.js`（基础配置）
- `postcss.config.js` / `tailwind.config.js`
- `app/layout.tsx`（Next App Router 根 Layout，用 DashboardLayout 包裹）
- `app/page.tsx`（根页面示例）
- `app/dashboard/page.tsx`、`app/analytics/page.tsx`、`app/settings/page.tsx`
- `src/components/layouts/DashboardLayout.tsx`（核心实现）
- `src/components/layouts/Sidebar.tsx`（可拆分）
- `src/components/layouts/Header.tsx`
- `src/components/ui/*`（示例：封装 Shadcn Button/Input/Avatar 引入的组件或直接使用 Shadcn 导入）
- `src/config/sidebar.ts`（菜单配置）
- `src/lib/theme.ts`（主题切换逻辑）
- `tests/sidebar.test.tsx`（示例测试）
- `README.md`

> 对每个文件，请给出完整代码（包含必要的 imports/exports）。若依赖某些图标，请使用 `lucide-react`。所有路径使用 TypeScript 导出格式。

## 4. 代码质量 & 约束（必须遵守）
- TypeScript 严格 `strict`：组件 props 明确声明类型
- 不使用 `any`（除非注释说明且无法避免）
- 所有交互元素使用可访问的 HTML 元素（button/label/nav）并包含必要的 aria 属性
- Tailwind 类从 `tailwind.config.js` 中声明并使用 `className` 合并工具（例如 `cn`/`clsx`），若引用 `cn`，请在 `src/lib/utils.ts` 提供实现
- 侧栏菜单项使用 `next/link` 做导航（App Router 下可使用 `Link`）
- 所有 Shadcn 组件使用其标准导入路径（示例可假设 `/components/ui/*` 封装好）

## 5. 输出格式（严格）
- 每个文件前用注释行 `// FILE: <path>` 标明文件路径
- 文件内容完整，从顶部 `import` 一直到 `export default` 或 `export`
- 在 `README.md` 中说明如何在本地运行（install / dev / build / test 命令）
- 在代码末尾提供一段“验证清单”（Check List），说明如何手动验证折叠、Drawer、主题、路由高亮等关键功能

## 6. 示例菜单配置（可直接用）
- Dashboard
- Analytics
  - Reports
  - Metrics
- Settings
- Help

## 7. 示例 AI 行为约束（对生成模型的额外提示）
- 优先保证“可复制运行”的完整代码；不要偷省细节
- 若某些第三方包需配置（如 Shadcn UI 的 CSS），请在 README 或注释中说明如何处理
- 如果需要创建辅助工具/小函数（如 `cn`、`useTheme`），一并生成
- 生成测试时请尽量模拟 DOM 行为（点击折叠按钮后期待的 class 或文本变化）

- 全部的shadcn ui 基础组件都安装好了 无需重复编写


  
## 8. 最终交付（示例：将要输出的内容）
- 从 `package.json` 开始逐个文件全部输出，格式如下：
  // FILE: package.json
  { ... }
  // FILE: next.config.js
  // FILE: tailwind.config.js
  // FILE: app/layout.tsx
  // FILE: src/components/layouts/DashboardLayout.tsx
  ...
- 最后附上 `README.md`，并包含“手动功能验证清单”



```







```javascript
核心技术栈:
- Next.js 15.5.4 (使用 App Router)
- React 19.1.0
- TypeScript
- TailwindCSS v4
- Shadcn/UI 组件库

全局layout

布局风格:

布局结构:

布局特点:

布局场景:

通用功能:

核心功能:

技术功能:

业务功能:


布局系统：
Zustand 进行状态管理
全局加载进度条


```





```javascript
A simple sidebar with navigation grouped by section
A sidebar with collapsible sections
A sidebar with submenus
A floating sidebar with submenus
A sidebar with collapsible submenus
A sidebar with submenus as dropdowns
A sidebar that collapses to icons
An inset sidebar with secondary navigation
Collapsible nested sidebars
A sidebar in a popover
A sidebar with a collapsible file tree
A sidebar with a calendar
A sidebar in a dialog
A sidebar on the right
A left and right sidebar
A sidebar with a sticky site header

翻译成为中文,这些分别是布局系统的什么属性?


| 英文原文                                                | 中文翻译           | 属于布局系统的什么属性             |
| --------------------------------------------------- | -------------- | ----------------------- |
| A simple sidebar with navigation grouped by section | 按区块分组导航的简单侧边栏  | **导航结构 / 信息分组**         |
| A sidebar with collapsible sections                 | 带可折叠分组的侧边栏     | **折叠 / 展开能力**           |
| A sidebar with submenus                             | 带子菜单的侧边栏       | **层级导航**                |
| A floating sidebar with submenus                    | 带子菜单的悬浮侧边栏     | **悬浮定位 / 弹出式层级导航**      |
| A sidebar with collapsible submenus                 | 带可折叠子菜单的侧边栏    | **多级折叠导航**              |
| A sidebar with submenus as dropdowns                | 子菜单以下拉形式展开的侧边栏 | **下拉式层级导航**             |
| A sidebar that collapses to icons                   | 可折叠成图标形式的侧边栏   | **极简模式 / 图标收纳**         |
| An inset sidebar with secondary navigation          | 带次级导航的嵌套式侧边栏   | **主次导航结构**              |
| Collapsible nested sidebars                         | 可折叠的嵌套侧边栏      | **多层侧边栏结构**             |
| A sidebar in a popover                              | 出现在浮层中的侧边栏     | **Popover 弹出式导航**       |
| A sidebar with a collapsible file tree              | 带可折叠文件树的侧边栏    | **树状结构导航**              |
| A sidebar with a calendar                           | 带日历组件的侧边栏      | **功能型侧栏（工具集成）**         |
| A sidebar in a dialog                               | 出现在对话框中的侧边栏    | **对话框模式侧栏**             |
| A sidebar on the right                              | 右侧侧边栏          | **位置属性（Right Sidebar）** |
| A left and right sidebar                            | 左右双侧边栏         | **双边导航布局**              |
| A sidebar with a sticky site header                 | 带粘性站点头部的侧边栏布局  | **固定头部 + 侧边组合布局**       |


结构类型（结构分层/主次导航/嵌套）
交互类型（折叠/悬浮/下拉/图标模式）
布局位置（左侧/右侧/双侧/浮层/对话框内）
功能扩展（文件树/日历等集成型侧栏）
仪表盘 / CMS / SaaS / 管理后台


  

```



```javascript
核心技术栈:
- Next.js 15.5.4 (使用 App Router)
- React 19.1.0
- TypeScript
- TailwindCSS v4
- Shadcn/UI 组件库

布局风格:
布局结构:
布局特点:
布局场景:
通用功能:
核心功能:
技术功能:
业务功能:
都有哪些?

好的，你现在是在整理前端布局系统/框架的能力清单结构模板，
我来把你列的分类项全部填充出常见项 + 可扩展方向，方便后续做成配置化/文档化模板。

核心技术栈:
Next.js 15.5.4（App Router）
React 19.1.0
TypeScript
TailwindCSS v4（支持 CSS 变量模式）
Shadcn/UI（可定制 UI 库）

布局风格 (Style)
扁平风 / 卡片式 / 毛玻璃 / Skeuomorphic / 极简极线条 / 暗色 / 浅色 / 企业管理风 / Dashboard 风格 / CMS 风格

布局结构 (Structure)
Header + Sidebar + Content / 
顶部导航 + 内容 / 
左右双侧栏 / 
顶部标签页式（Tabs）/ 
嵌套布局（Secondary Sidebar）/
Floating Sidebar /
Drawer式侧栏

布局特点 (Features)
响应式 / 侧栏可折叠 / 可拖动调整宽度 / 固定 Header / 固定 Breadcrumb / 粘性工具栏 / 支持多标签页 / 全屏切换 / 卡片网格


布局场景 (Use Cases)
管理后台 / 数据仪表盘 / CRM / ERP / 内容管理（CMS）/ SaaS 平台 / 开发者控制台 / 低代码平台 / 文件管理系统


通用功能 (Common Functions)
搜索框 / 全局通知 / 用户菜单 / Breadcrumb / 多语言切换 / 暗色模式切换 / 设置按钮 / Tab 路由导航

核心功能 (Core Layout Capabilities)
菜单权限控制 / 路由高亮 / 折叠菜单 / 面包屑自动生成 / 页面缓存（KeepAlive）/ 多标签页导航（TagView）/ 状态同步（URL+store）


技术功能 (Technical Utilities)
Layout 组件拆分 / Suspense + Skeleton Loading /
动态 Import /
Client/
Server Component 划分 / 
Head 元数据处理 / 
SEO结构布局 / 
Lazy Sidebar / 
动画过渡


```



```javascript
1. 项目基础信息
项目名称	
应用类型	如：Dashboard / SaaS / CMS / CRM
技术栈	Next.js 15 + React 19 + TS + TailwindCSS v4 + ShadCN UI


2. 布局体系总览
维度	选型 / 规则
布局结构	Sidebar + Header + Content
布局风格	扁平 / 卡片式 / 毛玻璃（任选其一或多主题）
响应式规则	lg: 以上为桌面，以下切换为 Drawer
侧边栏类型	固定 / 可折叠 / 可悬浮 / 带子菜单
头部类型	固定高度 / 可粘性 / 包含搜索 + 用户菜单

3. 布局模块定义
模块	职责	组件路径	交互规范
Sidebar	导航入口	/components/layouts/Sidebar.tsx	支持折叠 + 激活高亮
Header	全局操作区	/components/layouts/Header.tsx	包含搜索框 / 用户菜单
Content	页面内容	Layout children	背景灰，内部白卡片


4. 主题与色彩规范
元素	默认颜色	Tailwind Token
页面背景	#f5f5f5	bg-gray-100
白色容器	#ffffff	bg-white
主色（Primary）	示例：#3b82f6	text-primary / bg-primary
激活菜单色	自动 from ShadCN variant="default"	-

5. 间距与尺寸规范
元素	高度/宽度	Tailwind 值
Header 高度	64px	h-16
Sidebar 宽度	展开 240px / 折叠 64px	w-60 / w-16
Page Padding	24px	p-6
Card Padding	24px	p-6

6. 响应式规范
设备	断点	调整内容
手机	<lg	Sidebar 切换为 Drawer
平板	lg~xl	正常布局
大屏	xl~2xl	可增加左右留白
  
7. 通用交互规范
功能	行为规则
菜单激活高亮	使用 variant="default"
点击菜单切换页面	使用 next/link 包裹按钮
折叠侧边栏	Hover 有 Tooltip
搜索框	回车触发搜索事件

8. 代码约定规范

✅ 推荐使用 独立 Layout 组件 + Slot children 渲染页面




```





```javascript
会有哪些 技术功能: 业务功能

✅ 技术功能（Technical Layout Features）

这些主要是为提升性能、可维护性与开发效率：

功能类型	功能项
渲染性能优化	Suspense + Skeleton Loading、Lazy Sidebar（动态加载菜单）、Dynamic Import 子模块
状态与路由联动	菜单高亮自动匹配路由、面包屑自动推导、Tab 多页签缓存（KeepAlive）
权限控制	菜单基于权限渲染 / 路由守卫 / 按钮级权限控制
响应式与自适应	Sidebar 支持折叠 / Drawer 模式切换 / 缩放适应大屏
动画与交互增强	折叠动画、悬停 Tooltip、Transition 控制
布局配置化	JSON 定义侧栏结构 → 自动渲染布局
可插拔布局模块	Layout Header / Sidebar 可动态替换
主题系统	明暗模式切换 / CSS Variables 控制全局色彩
国际化支持	Layout 内置语言切换（多语言 Sidebar / Header）
可访问性（A11y）	键盘导航支持（Tab Focus）、ARIA 标签自动添加


✅ 业务功能（Business-Oriented Layout Widgets）

这些是实际业务系统常见的“复用型界面模块”：

功能类型	业务部件
通用信息展示	统计数据卡片（KPI Card）、通知中心、进度条栏
操作快捷入口	最近操作记录 / 常用功能收藏栏 / 快捷创建按钮（+）
搜索与筛选模块	全局搜索框 / 表格筛选器 FilterBar / 条件标签
表单型布局	两栏/三栏表单布局、抽屉表单、分步表单
导航增强	面包屑 Breadcrumb、Tab 多标签页、步骤面板 Steps 导航
文件/数据管理类	树形目录 Sidebar（如文件管理）、日历 Sidebar、时间线
审批/流程控件	步骤状态栏、Timeline 历史记录、流程图可视化嵌入
互动类模块	聊天侧栏 / 用户列表 / 评论区 Dock
运营/AI 增强	AI 助手悬浮 Dock、右侧推荐信息栏（Context Info）







```



```javascript
✅ 代码设计规范 / 原则（建议用于团队项目或个人长期维护项目）
1️⃣ 目录结构规范
按功能/领域划分（Feature-based）优先于按技术划分
单一职责/模块划分清楚/可维护强/避免一个包中放了很多代码文件
components / hooks / utils 必须具备明确命名，不允许“misc / common / temp”
文件命名统一小写短横线（kebab-case）

2️⃣ 编码风格
必须使用 ESLint + Prettier 自动化
禁止使用 any（除非写明原因）
前端组件必须使用命名导出，禁止 default export（更利于重构）
常量、枚举、接口统一使用 PascalCase / UPPER_SNAKE_CASE

3️⃣ 组件设计原则
组件要么是「展示型（Presentational）」要么是「容器型（Container）」
组件应支持可扩展性：接收 className / style / children
UI 组件禁止直接写业务逻辑，业务逻辑应封装为 hooks / utils

4️⃣ CSS / Tailwind 规范
禁止写纯 CSS 文件（除非全局变量）
复用样式用 cn() 合并，不要出现重复样式拼接
可读性优先于极端压缩：合理换行排版

5️⃣ 状态管理原则
组件内部用 useState
页面共享逻辑用 useContext / custom hooks
全局状态才用 Zustand / Redux / Jotai

6️⃣ API 调用规范
所有 API 必须封装在 /lib/api / /services 中
禁止在组件中出现 fetch('/api/...') 字符串

7️⃣ 错误处理与边界
所有异步操作必须做异常捕获
UI 组件必须有 Loading / Empty / Error 状态

8️⃣ 可访问性（Accessibility）
ShadCN 组件默认支持，可确保 semantic HTML
任何可点击元素必须为 <button> 或 <a>，禁止 div

9️⃣ 文档与注释
复杂逻辑必须写 // WHY: 注释，而不是 // WHAT:
可选功能点写 // TODO: 并统一追踪
```








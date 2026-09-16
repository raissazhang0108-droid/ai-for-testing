# AI-TestSphere

<p align="right">
  <a href="./README.md">English</a> | <b>简体中文</b>
</p>

<p align="center">
  <img src="https://shields.io" alt="PRs Welcome">
  <img src="https://shields.io" alt="Python Version">
  <img src="https://shields.io" alt="Framework Type">
  <img src="https://shields.io" alt="License">
</p>

**AI-TestSphere** 是一款下一代、基于大语言模型（LLM）驱动的全栈智能自动化测试框架。项目打破了传统自动化测试“重手工维护、脚本易脆弱断裂”的僵局，将 AI 能力深度注入到测试全生命周期中。

> 💡 **项目初心**：本项目旨在探索 AI4SE（AI 辅助软件工程）在质量保障领域的工业级落地。架构设计紧扣大厂核心业务场景，不仅是一个开箱即用的智能化测试工具箱，更是一个完美的**高级测试开发 / 测开架构师面试技术演练场**。

---

## 🚀 核心架构与十一大 AI 测试场景

本项目打破了传统自动化测试工程的局限，将大语言模型与传统测试底座深度融合，覆盖测试全生命周期的 **11 大核心 AI 智能化场景**：

### 1. 📋 AI 需求分析
* **多源输入解析**：支持 PRD 文档、Axure/Figma 原型图一键输入。
* **结构化评审**：基于 LLM 进行需求全要素（IEEE 29148 规范）自动抽取，智能识别隐式需求与逻辑漏洞。

### 2. ✍️ 智能测试用例编写
* **用例大脑**：自动根据结构化需求拆解整体测试骨架，运用“链路基线法+多维边界值矩阵”生成高覆盖率用例。
* **格式自适应**：支持一键导出为标准 Mindmap（思维导图）、Excel 或 JSON 评审表。

### 3. 🔍 增量代码变更分析
* **变更血缘追踪**：通过静态代码分析与 AST 树比对，精准定位代码变更所隐式影响的业务上游与下游。
* **回归范围瘦身**：AI 动态规划最优回归测试集，拒绝盲目全量测试。

### 4. ⚙️ 智能测试用例执行
* **多模式调度**：支持无头（Headless）串行、多进程并行执行。
* **执行期快照**：支持自动化过程中的全链路 Trace、全量日志采集与关键步骤自动截屏/录屏。

### 5. 📊 高可视化测试报告生成
* **多维聚合报告**：原生集成 Allure HTML 智能报告，支持历史趋势续传与模块化聚合。
* **AI 报告摘要**：大模型自动提炼执行盲区、频发故障模块，并为研发团队生成直观的质量周报。

### 6. 🎯 深度测试覆盖率分析
* **双端覆盖率度量**：融合代码层（Jacoco/Coverage.py 语句及分支覆盖率）与业务功能需求层双重覆盖率。
* **盲区漏测预警**：AI 交叉对比测试结果与变更代码，精准指出未被用例覆盖的“死角代码”。

### 7. 💾 智能数据库验证 & Text2SQL
* **Text2SQL 验证**：测试人员输入自然语言，AI 自动转化为多方言可执行 SQL 并进行数据断言。
* **测试沙箱护栏**：具备全隐写引擎与数据安全护栏，确保数据构建与清理的幂等性与安全性。

### 8. 🚨 智能 Bug 根因分析
* **自动化日志归因**：当测试失败时，AI 提取 `logcat`、`syslog` 或 `crashlog` 并进行多分类（Android 6类 / iOS 9类）。
* **修复建议生成**：大模型精确定位报错代码行，并自动生成修复建议（PR 补丁建议）。

### 9. 🌐 AI 接口自动化
* **抓包逆向工程**：一键解析 HAR/Charles 抓包数据，反向生成 OpenAPI 3.0 规范文档与动态参数化 Mock 脚本。
* **智能场景组合**：AI 理解接口上下文血缘，自动组合编排单接口至多接口的复杂业务场景链路。

### 10. 🤖 具备自愈能力的 UI 自动化
* **Playwright 智能驱动**：基于高级 Page Object 模式的分层设计。
* **DOM 智能自愈**：当页面元素因前端迭代定位变更时，Agent 自动启动“收证 -> 相似度重定性 -> 最小改动运行 -> 自动重写定位表达式”的闭环自愈机制。

### 11. 📱 AI 移动端 APP 自动化
* **跨平台双底座**：完美适配 Appium（Android 混合应用定位金字塔）与 XCTest（iOS WDA 真机签名适配）。
* **快照工程化**：通过界面快照（Screenshot & Hierarchy），AI 自动识别界面元素并自动翻译为标准自动化测试脚本。

---

## 📂 项目目录结构

```text
your-repo/
├── config/             # 大模型基座配置与 Prompt 模板
├── core/               # 框架底层核心 Agent 路由与执行引擎
├── modules/            # 11 大 AI 驱动的核心测试能力模块
│   ├── requirement/    # 01. 需求分析
│   ├── generator/      # 02. 测试用例生成
│   ├── impact/         # 03. 代码变更分析
│   ├── executor/       # 04. 智能用例执行
│   ├── reporter/       # 05. 测试报告生成
│   ├── coverage/       # 06. 测试覆盖率分析
│   ├── database/       # 07. 数据库验证 & Text2SQL
│   ├── triaging/       # 08. Bug 根因归因
│   ├── api/            # 09. 接口自动化
│   ├── web_ui/         # 10. UI 自动化 (自愈能力)
│   └── mobile/         # 11. APP 自动化
├── tests/              # 框架自测用例
└── README.md
```

---

## ⚡ 快速开始

### 1. 克隆项目与环境安装
```bash
git clone https://github.com
cd your-repo
pip install -r requirements.txt
playwright install
```

### 2. 配置环境变量
在项目根目录下创建 `.env` 文件：
```env
OPENAI_API_BASE="https://your-provider.com"
OPENAI_API_KEY="your-api-key-here"
LLM_MODEL="deepseek-chat"
```

---

## 📄 开源协议
本项目基于 [MIT License](LICENSE) 协议开源。

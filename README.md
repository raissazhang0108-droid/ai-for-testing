# AI-For-Testing

<p align="right">
  <b>English</b> | <a href="./README_CN.md">简体中文</a>
</p>

<p align="center">
  <img src="https://shields.io" alt="PRs Welcome" />
  <img src="https://shields.io" alt="Python Version" />
  <img src="https://shields.io" alt="Framework Type" />
  <img src="https://shields.io" alt="License" />
</p>

**AI-TestSphere** is a next-generation, full-stack automation testing framework driven by Large Language Models (LLMs). It breaks the constraints of traditional automation testing—such as high maintenance costs and fragile script locators—by injecting AI into every phase of the testing lifecycle.

> 💡 **Project Vision**: Designed to explore the industrial implementation of AI4SE (AI for Software Engineering) in quality assurance. The architecture tightly aligns with top-tier tech enterprise production scenarios, making it both a turnkey intelligent toolkit and a perfect **technical playground for Senior QA Engineer / QA Architect interviews**.

---

## 🚀 Core Architecture & 11 Major AI Testing Scenarios

This framework breaks the constraints of traditional automation testing by deeply integrating Large Language Models (LLMs) with robust testing bedrock. It covers **11 core AI-powered intelligent scenarios** across the entire testing lifecycle:

### 1. 📋 AI Requirement Analysis
* **Multi-Source Parsing**: Supports one-click ingestion of PRD text documents, as well as Axure and Figma interactive prototypes.
* **Structured Review**: Utilizes LLMs to automatically extract requirement key elements (aligned with IEEE 29148 standards) to spot implicit requirements and logical loopholes.

### 2. ✍️ AI-Powered Test Case Generation
* **Test Design Brain**: Automatically constructs the main testing framework from structured requirements, applying "link baseline analysis + multi-dimensional boundary value matrix" to generate high-coverage test cases.
* **Flexible Export**: Supports exporting test suites directly into Mindmaps, Excel sheets, or standard JSON definitions for peer reviews.

### 3. 🔍 AI Change Impact Analysis
* **Change Lineage Tracking**: Pinpoints upstream and downstream business logic implicitly affected by code changes using static analysis and Abstract Syntax Tree (AST) comparisons.
* **Regression Slimming**: Dynamically schedules the optimal subset of regression tests to avoid redundant full-suite executions.

### 4. ⚙️ Smart Case Execution
* **Multi-Mode Scheduling**: Supports cross-platform execution, including headless serial runs and multi-process parallel processing.
* **Execution Traceability**: Captures full-link traces, complete console logs, and automated screenshots/videos for critical validation steps.

### 5. 📊 AI Test Reporting
* **Aggregated Analytics**: Native integration with Allure HTML reports to maintain history trends and modular component matrices.
* **AI Quality Summarization**: Automatically synthesizes execution blind spots and high-frequency defect modules into human-readable executive quality summaries.

### 6. 🎯 AI-Enhanced Coverage Analysis
* **Dual-Layer Coverage**: Combines code-level coverage (statement/branch metrics via Jacoco or Coverage.py) with functional requirement coverage maps.
* **Blind Spot Alerts**: Cross-references test results against code changes to actively warn teams of uncovered "dead zones."

### 7. 💾 AI Database Verification & Text2SQL
* **Text2SQL Assertion**: Translates natural language queries into dialect-compliant executable SQL to perform precise data state assertions.
* **Data Guardrails**: Built-in data masking engines and strict idempotency rules to ensure secure data setup and teardown within the testing sandbox.

### 8. 🚨 AI Defect Triaging & Root Cause Analysis
* **Automated Log Attribution**: Upon execution failures, AI analyzes `logcat`, `syslog`, or `crashlog` artifacts to categorize root causes (e.g., 6 classes for Android, 9 for iOS).
* **Fix Suggestions**: Precisely maps stack traces to code lines, generating automated code patch suggestions for developers.

### 9. 🌐 AI-Driven API Testing
* **Traffic Reverse Engineering**: Parses HAR/Charles network captures to automatically generate OpenAPI 3.0 documentation and dynamic parameterized mock servers.
* **Intelligent Scenario Chaining**: Understands API data lineage to dynamically chain single endpoints into complex, multi-stage business workflows.

### 10. 🤖 Self-Healing Web UI Automation
* **Playwright Core**: Built upon a mature Page Object Model (POM) layer for robust multi-browser execution.
* **Locator Self-Healing**: If web elements shift due to UI updates, an AI Agent initiates a self-healing loop: "collect evidence -> calculate structural similarity -> run patch -> rewrite locator expressions."

### 11. 📱 AI Mobile Automation
* **Dual-Platform Bedrock**: Fully compatible with Appium (Android hybrid locator pyramids) and XCTest (iOS WDA real-device provisioning).
* **UI Snapshot Engineering**: Analyzes mobile screenshots and XML hierarchies to automatically identify interactive elements and translate them into executable automation scripts.

---

## 📂 Repository Structure

```text
your-repo/
├── config/             # LLM provider base configurations & prompts
├── core/               # Framework core routing & orchestrator engines
├── modules/            # 11 AI-driven core testing capability modules
│   ├── requirement/    # 01. Requirement Analysis
│   ├── generator/      # 02. Test Case Generation
│   ├── impact/         # 03. Change Impact Analysis
│   ├── executor/       # 04. Smart Case Execution
│   ├── reporter/       # 05. AI Test Reporting
│   ├── coverage/       # 06. Coverage Analysis
│   ├── database/       # 07. Database & Text2SQL
│   ├── triaging/       # 08. Defect Root Cause Analysis
│   ├── api/            # 09. API Testing
│   ├── web_ui/         # 10. Self-Healing Web UI
│   └── mobile/         # 11. Mobile Automation
├── tests/              # Test cases for the framework itself
└── README.md
```

---

## ⚡ Quick Start

### 1. Clone & Install
```bash
git clone https://github.com
cd your-repo
pip install -r requirements.txt
playwright install
```

### 2. Configuration
Create a `.env` file in the root directory:
```env
OPENAI_API_BASE="https://your-provider.com"
OPENAI_API_KEY="your-api-key-here"
LLM_MODEL="deepseek-chat"
```

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).

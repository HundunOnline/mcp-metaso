# 变更日志

本文档记录了项目的所有重要变更。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
并且本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/) 规范。

## [1.0.0] - 2025-07-24

### 🎉 首次发布

这是首个公开发布版本，基于 MCP FastMCP SDK 构建。

### ✨ 新增功能

- **多维搜索支持**：支持 6 种不同的搜索类型
  - 网页搜索 (webpage)
  - 文库搜索 (document)
  - 学术搜索 (scholar)
  - 图片搜索 (image)
  - 视频搜索 (video)
  - 播客搜索 (podcast)
- **网页解析工具**：支持 Markdown 和 JSON 格式输出
- **FastMCP 集成**：使用官方 MCP FastMCP SDK
- **类型安全**：完整的类型注解和自动参数验证
- **异步处理**：高性能异步 API 调用
- **智能格式化**：针对不同搜索类型的专业格式化
- **错误处理**：完善的异常捕获和错误响应
- **测试套件**：全面的功能测试脚本

### 🔧 技术特性

- 基于 Python 3.10+ 
- 使用 MCP 1.1.0+ 和 FastMCP SDK
- HTTP 客户端使用 httpx 进行高性能请求
- 支持 Claude Desktop 等 MCP 客户端集成
- 最小化依赖，快速部署

### 📚 文档

- 详细的 README 文档
- 完整的 API 参考
- Claude Desktop 集成指南
- 开发者指南和最佳实践

### 🚀 部署

- 支持 pip 安装
- 环境变量配置
- 一键启动服务器
- Docker 友好

---

## 开发历史

在正式发布之前，项目经历了多个开发阶段：

### v0.4.0-dev - 多维搜索重构
- 新增 6 种搜索类型支持
- 智能结果格式化系统
- 完善的测试覆盖

### v0.3.0-dev - FastMCP 迁移
- 从手动 JSON-RPC 迁移到 FastMCP SDK
- 代码量减少 50%
- 自动 schema 生成

### v0.2.0-dev - MCP 集成
- 集成 MCP 官方 SDK
- 标准化协议实现

### v0.1.0-dev - 原型版本
- 基础 Metaso API 集成
- 手动 JSON-RPC 实现
- 仅支持网页搜索

---

## 贡献指南

有关如何为本项目贡献代码，请参阅我们的 [贡献指南](CONTRIBUTING.md)。

## 许可证

本项目采用 [MIT 许可证](LICENSE)。 
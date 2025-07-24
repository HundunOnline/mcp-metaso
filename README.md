# MCP Metaso

> 一个基于 [MCP (Model Context Protocol)](https://modelcontextprotocol.io/) 的 Metaso AI 搜索引擎服务器，使用官方 FastMCP SDK 构建。

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![MCP](https://img.shields.io/badge/MCP-1.1.0+-green.svg)](https://modelcontextprotocol.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## ✨ 功能特性

- 🔍 **多维搜索**：支持网页、文库、学术、图片、视频、播客六种搜索类型
- 📄 **网页解析**：提取网页内容并转换为 Markdown 或 JSON 格式
- ⚡ **高性能**：基于 FastMCP SDK，异步处理，类型安全
- 🔌 **标准兼容**：完全符合 MCP 协议规范，可与 Claude Desktop 等客户端集成

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置 API 密钥

```bash
export METASO_API_KEY="your-api-key-here"
```

### 3. 启动服务器

```bash
python server.py
```

### 4. 测试功能

```bash
python test_all_scopes.py
```

## 🔧 Claude Desktop 集成

在 Claude Desktop 配置文件中添加：

```json
{
  "mcpServers": {
    "mcp-metaso": {
      "command": "python",
      "args": ["/path/to/mcp-metaso/server.py"],
      "env": {
        "METASO_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

配置文件位置：
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

## 📖 可用工具

### metaso_search

多维搜索工具，支持六种搜索类型：

```python
metaso_search(
    query="人工智能发展趋势",  # 搜索查询词
    scope="webpage",           # 搜索类型：webpage/document/scholar/image/video/podcast
    include_summary=False,     # 是否包含 AI 摘要
    size=10                   # 结果数量 (1-20)
)
```

**搜索类型说明：**
- `webpage` - 网页搜索：新闻、博客、资讯
- `document` - 文库搜索：PDF 文档、技术文档
- `scholar` - 学术搜索：论文、研究文献
- `image` - 图片搜索：图片、图表、插图
- `video` - 视频搜索：教程、演讲、娱乐内容
- `podcast` - 播客搜索：音频节目、访谈

### metaso_reader

网页内容解析工具：

```python
metaso_reader(
    url="https://example.com",  # 网页 URL
    output_format="markdown"    # 输出格式：markdown/json
)
```

## 📁 项目结构

```
mcp-metaso/
├── server.py              # 主服务器实现 (FastMCP)
├── config.py              # 配置管理
├── test_all_scopes.py     # 功能测试脚本
├── requirements.txt       # 项目依赖
├── setup.py              # 包安装配置
└── README.md             # 项目说明
```

## 🔨 开发

### 环境要求

- Python 3.10+
- Metaso API Key

### 本地开发

1. 克隆项目：
   ```bash
   git clone <repository-url>
   cd mcp-metaso
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

3. 设置环境变量：
   ```bash
   export METASO_API_KEY="your-key"
   ```

4. 运行测试：
   ```bash
   python test_all_scopes.py
   ```

### 添加新功能

使用 FastMCP 装饰器可以轻松添加新工具：

```python
@mcp.tool()
async def new_tool(param: str) -> str:
    """新工具描述
    
    Args:
        param: 参数描述
    """
    # 实现逻辑
    return result
```

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE)。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 🔗 相关链接

- [MCP 官方文档](https://modelcontextprotocol.io/)
- [FastMCP SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Metaso AI](https://metaso.cn/) 
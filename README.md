# MCP Metaso

> 一个基于 [MCP (Model Context Protocol)](https://modelcontextprotocol.io/) 的 Metaso AI 搜索引擎服务器，使用官方 FastMCP SDK 构建。

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![MCP](https://img.shields.io/badge/MCP-1.1.0+-green.svg)](https://modelcontextprotocol.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![smithery badge](https://smithery.ai/badge/@HundunOnline/mcp-metaso)](https://smithery.ai/server/@HundunOnline/mcp-metaso)

## ✨ 功能特性

- 🔍 **多维搜索**：支持网页、文库、学术、图片、视频、播客六种搜索类型
- 📄 **网页解析**：提取网页内容并转换为 Markdown 或 JSON 格式
- ⚡ **高性能**：基于 FastMCP SDK，异步处理，类型安全
- 🔌 **标准兼容**：完全符合 MCP 协议规范，可与 Claude Desktop 等客户端集成

## 🚀 快速开始

### 安装依赖

#### Installing via Smithery

To install mcp-metaso for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@HundunOnline/mcp-metaso):

```bash
npx -y @smithery/cli install @HundunOnline/mcp-metaso --client claude
```

#### 手动安装

```bash
pip install -r requirements.txt
```

### 配置 API 密钥

```bash
export METASO_API_KEY="your-api-key-here"
```

### 启动服务器

```bash
python server.py
```

### 测试功能

```bash
python test_all_scopes.py
```

## 🔧 Claude Desktop 集成

### DXT扩展安装（最简单的方式）🌟

Claude Desktop现在支持DXT扩展格式，让安装变得像安装浏览器扩展一样简单！

1. **下载DXT扩展文件**
   - 从[发布页面](https://github.com/HundunOnline/mcp-metaso/releases)下载 `mcp-metaso-1.1.0.dxt`

2. **双击安装**
   - 打开Claude Desktop应用
   - 导航到 **设置 > 扩展**
   - 点击"从.dxt文件安装"并选择下载的文件
   - 在配置界面输入您的Metaso API密钥
   - 点击"安装"完成

3. **立即使用**
   - 重启Claude Desktop
   - 开始使用："搜索人工智能的最新发展"

### 自动安装工具（传统方式）

如果您更喜欢传统的安装方式：

```bash
# 自动安装到Claude Desktop
python tools/install_claude.py

# 或使用配置生成器
python tools/claude_config_generator.py --save
```

### 手动配置

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

**配置文件位置：**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

### 验证配置

安装完成后，验证配置是否正确：

```bash
# 验证MCP服务器配置
python tools/validate_config.py

# 生成诊断报告
python tools/validate_config.py --report
```

### 故障排除

如果Claude Desktop没有显示🔨图标：

1. **重启Claude Desktop** - 配置更改需要重启应用
2. **检查路径** - 确保使用绝对路径指向server.py
3. **验证API密钥** - 确保METASO_API_KEY已正确设置
4. **查看日志** - 检查Claude Desktop日志文件夹中的错误信息

**常用工具命令：**
```bash
# 生成配置
python tools/claude_config_generator.py --api-key your_key --save

# 自动安装
python tools/install_claude.py --auto-confirm

# 卸载服务器
python tools/install_claude.py --uninstall

# 验证配置
python tools/validate_config.py

# 使用启动包装器
python tools/launcher.py
```

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
├── server.py                      # 主服务器实现 (FastMCP)
├── config.py                      # 配置管理
├── tools/                         # Claude Desktop集成工具
│   ├── __init__.py               # 工具包初始化
│   ├── claude_config_generator.py # Claude配置生成器
│   ├── install_claude.py         # 自动安装脚本
│   ├── validate_config.py        # 配置验证工具
│   └── launcher.py               # 启动包装器
├── test_all_scopes.py            # 功能测试脚本
├── requirements.txt              # 项目依赖
├── setup.py                      # 包安装配置
└── README.md                     # 项目说明
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

### 构建DXT扩展

开发者可以构建DXT扩展包：

```bash
# 构建DXT扩展包
python build-dxt.py

# 这将生成：
# - mcp-metaso-1.1.0.dxt (扩展包)
# - DXT安装指南.md (用户安装说明)
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
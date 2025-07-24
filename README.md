# MCP Metaso AI搜索服务器

这是一个基于MCP (Model Context Protocol) **官方FastMCP SDK**的AI搜索服务器，集成了Metaso AI搜索引擎的多维度搜索和网页解析功能。

## ✨ 最新版本亮点

**使用MCP官方FastMCP SDK重构 - 更稳定、更简洁、更易维护！**

- 🚀 **FastMCP API**: 使用MCP官方推荐的高级FastMCP API
- 🎯 **自动工具注册**: 使用装饰器自动注册工具和生成schema
- 🛡️ **类型安全**: 完整的类型注解和自动参数验证
- 📉 **代码精简**: 从238行减少到120行，减少了50%的代码量
- 🔄 **自动处理**: SDK自动处理协议通信、错误管理和服务器初始化
- 🧪 **易于测试**: 内置测试脚本验证功能
- 🌐 **多维搜索**: 支持6种不同类型的搜索scope

## 功能特性

- 🔍 **多维AI搜索**：支持网页、文库、学术、图片、视频、播客六种搜索类型
- 📄 **网页解析**：提取网页内容并转换为Markdown或JSON格式
- ⚡ **高性能**：异步处理，支持并发请求
- 🔌 **标准兼容**：完全符合MCP协议规范
- ⚙️ **智能适配**：自动适配不同类型搜索结果的格式
- 🛡️ **错误处理**：完善的异常捕获和错误信息返回

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置API密钥

设置Metaso API密钥环境变量：

```bash
export METASO_API_KEY="your-api-key-here"
```

Windows用户：
```cmd
set METASO_API_KEY=your-api-key-here
```

### 3. 测试安装

运行全面测试脚本：

```bash
python test_all_scopes.py
```

或基础测试：

```bash
python test_server.py
```

### 4. 启动服务器

```bash
python server.py
```

## 可用工具

### 1. metaso_search - 多维AI搜索

使用Metaso AI搜索引擎进行多类型智能搜索。

**参数：**
- `query` (必需): 搜索查询词或问题
- `scope` (可选): 搜索类型，支持以下6种：
  - `webpage`（网页）- 默认值，搜索网页内容
  - `document`（文库）- 搜索文档库资源
  - `scholar`（学术）- 搜索学术论文和研究
  - `image`（图片）- 搜索图片资源
  - `video`（视频）- 搜索视频内容
  - `podcast`（播客）- 搜索播客节目
- `include_summary` (可选): 是否包含AI生成的搜索摘要，默认false
- `size` (可选): 返回结果数量，范围1-20，默认10

**搜索类型详解：**

#### 🌐 网页搜索 (webpage)
```json
{
  "query": "2024年人工智能发展趋势",
  "scope": "webpage",
  "include_summary": true,
  "size": 5
}
```
**返回格式**：标题、URL、摘要、发布时间

#### 📚 文库搜索 (document)
```json
{
  "query": "机器学习算法",
  "scope": "document",
  "size": 5
}
```
**返回格式**：标题、来源、URL、摘要、作者、发布时间

#### 🎓 学术搜索 (scholar)
```json
{
  "query": "deep learning transformer",
  "scope": "scholar",
  "size": 5
}
```
**返回格式**：标题、作者、期刊/会议、URL、摘要、发表年份、引用次数、DOI

#### 🖼️ 图片搜索 (image)
```json
{
  "query": "猫咪",
  "scope": "image",
  "size": 10
}
```
**返回格式**：图片URL、来源页面、标题、尺寸、缩略图、描述

#### 🎬 视频搜索 (video)
```json
{
  "query": "编程教程",
  "scope": "video",
  "size": 5
}
```
**返回格式**：标题、URL、描述、频道、时长、发布时间、观看次数、缩略图

#### 🎙️ 播客搜索 (podcast)
```json
{
  "query": "科技播客",
  "scope": "podcast",
  "size": 5
}
```
**返回格式**：标题、播客名称、URL、描述、主持人、时长、发布时间、音频链接

### 2. metaso_reader - 网页解析

解析网页内容并提取结构化文本。

**参数：**
- `url` (必需): 要解析的网页URL
- `output_format` (可选): 输出格式，支持"markdown"（默认）或"json"

**示例：**
```json
{
  "url": "https://example.com/article",
  "output_format": "markdown"
}
```

## MCP客户端集成

### Claude Desktop配置

在Claude Desktop的配置文件 (`~/Library/Application Support/Claude/claude_desktop_config.json`) 中添加：

```json
{
  "mcpServers": {
    "mcp-metaso": {
      "command": "python",
      "args": ["/path/to/your/mcp-metaso/server.py"],
      "env": {
        "METASO_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

### 使用示例

在Claude Desktop中，你可以这样使用：

```
请帮我搜索关于"量子计算"的学术论文
```

```
找一些编程相关的视频教程
```

```
搜索一些关于AI的播客节目
```

## 项目结构

```
mcp-metaso/
├── server.py              # 主服务器实现（使用FastMCP SDK）
├── config.py              # 配置管理
├── test_server.py         # 基础功能测试脚本
├── test_all_scopes.py     # 全面scope测试脚本
├── requirements.txt       # 项目依赖
├── setup.py              # 包安装配置
├── README.md             # 项目说明
├── USAGE.md              # 详细使用指南
└── mcp_metaso.egg-info/  # 包信息
```

## 开发和扩展

### 添加新工具

使用FastMCP添加新工具非常简单：

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my-server")

@mcp.tool()
async def my_new_tool(param1: str, param2: int = 10) -> str:
    """工具描述会自动成为工具的description
    
    Args:
        param1: 参数1的描述
        param2: 参数2的描述，有默认值
    """
    return f"处理结果: {param1} - {param2}"

if __name__ == "__main__":
    mcp.run()
```

### 添加新的搜索类型

要添加新的搜索scope：

1. 在 `SCOPE_RESULT_MAPPING` 中添加映射
2. 创建对应的格式化函数
3. 在 `RESULT_FORMATTERS` 中注册函数
4. 更新文档

```python
# 1. 添加映射
SCOPE_RESULT_MAPPING["news"] = "news"

# 2. 创建格式化函数
def format_news_result(item: dict, index: int) -> str:
    # 实现新闻结果格式化
    pass

# 3. 注册格式化函数
RESULT_FORMATTERS["news"] = format_news_result
```

## 核心优势

### 与旧实现对比

| 特性 | 旧实现 | 新实现（FastMCP + 多scope） |
|------|--------|---------------------------|
| 代码行数 | 238行 | 200行 |
| 搜索类型 | 仅网页 | 6种类型 |
| 协议处理 | 手动JSON-RPC | 自动处理 |
| 工具定义 | 手动schema | 装饰器+自动生成 |
| 结果格式 | 单一格式 | 智能适配 |
| 类型检查 | 手动验证 | 自动类型验证 |
| 错误处理 | 手动实现 | SDK内置 |
| 启动方式 | 复杂配置 | 一行代码 |

### 技术特点

- ⚡ **零配置启动**: `mcp.run()` 一行代码启动
- 🔧 **装饰器工具**: `@mcp.tool()` 自动注册
- 📊 **自动schema**: 从类型注解生成JSON schema
- 🛡️ **类型安全**: 运行时类型验证
- 🔄 **同步接口**: 内部自动处理异步操作
- 🎯 **智能路由**: 自动适配不同搜索类型

## 错误处理

新实现提供了完善的错误处理：

- **参数验证错误**：自动验证输入参数类型和范围
- **Scope验证**：检查搜索类型是否支持
- **HTTP请求错误**：网络连接和API调用错误
- **数据解析错误**：响应数据格式问题
- **系统异常**：意外错误的统一处理

## 性能特点

- ⚡ **异步处理**：内部使用 asyncio 支持高并发
- 📦 **轻量级**：最小化依赖，快速启动
- 🔄 **连接复用**：httpx 客户端连接池优化
- 💾 **内存友好**：自动资源管理
- 🎯 **智能缓存**：避免重复的API调用

## 版本历史

- **v0.4.0** - 新增多维搜索支持，支持6种不同的搜索类型
- **v0.3.0** - 使用FastMCP SDK重构，大幅简化代码和提升开发体验
- **v0.2.0** - 使用MCP官方SDK重构，提升稳定性
- **v0.1.0** - 初始版本，手动实现JSON-RPC协议

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request！请确保：

1. 代码通过类型检查
2. 添加适当的测试
3. 更新相关文档
4. 遵循FastMCP最佳实践
5. 测试所有相关的搜索scope 
# 贡献指南

感谢您对 MCP Metaso 项目的兴趣！我们欢迎所有形式的贡献。

## 🤝 如何贡献

### 报告问题

如果您发现了错误或有改进建议：

1. 首先搜索 [现有 Issues](https://github.com/your-username/mcp-metaso/issues) 确认问题未被报告
2. 创建新的 Issue，请包含：
   - 清晰的问题描述
   - 重现步骤
   - 期望的行为
   - 实际的行为
   - 环境信息（Python 版本、操作系统等）

### 提交代码

1. **Fork 项目**
   ```bash
   git clone https://github.com/your-username/mcp-metaso.git
   cd mcp-metaso
   ```

2. **创建分支**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **设置开发环境**
   ```bash
   pip install -r requirements.txt
   pip install -e ".[dev]"  # 安装开发依赖
   ```

4. **进行更改**
   - 遵循现有的代码风格
   - 添加必要的测试
   - 更新文档（如果需要）

5. **运行测试**
   ```bash
   python test_all_scopes.py  # 功能测试
   # 如果有其他测试，也请运行
   ```

6. **提交更改**
   ```bash
   git add .
   git commit -m "feat: 添加新功能描述"
   ```

7. **推送并创建 Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

## 📝 代码规范

### Python 代码风格

- 遵循 [PEP 8](https://peps.python.org/pep-0008/) 规范
- 使用类型注解
- 函数和类需要有完整的 docstring
- 变量和函数命名使用英文

### 提交信息规范

使用以下格式：

```
type(scope): description

[optional body]

[optional footer]
```

**类型 (type):**
- `feat`: 新功能
- `fix`: 错误修复
- `docs`: 文档更新
- `style`: 代码格式调整
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建过程或辅助工具的变动

**示例:**
```
feat(search): 添加图片搜索功能

- 新增 image scope 支持
- 添加图片结果格式化器
- 更新测试用例

Closes #123
```

## 🧪 测试

### 运行测试

```bash
# 基础功能测试
python test_all_scopes.py

# 如果添加了新的测试文件
python -m pytest tests/
```

### 添加测试

- 为新功能添加相应的测试
- 确保测试覆盖率不下降
- 测试应该快速且独立

## 📋 开发设置

### 环境要求

- Python 3.10+
- 有效的 Metaso API 密钥

### 本地开发

1. **安装依赖**
   ```bash
   pip install -r requirements.txt
   pip install -e ".[dev]"
   ```

2. **设置环境变量**
   ```bash
   export METASO_API_KEY="your-test-api-key"
   ```

3. **运行服务器**
   ```bash
   python server.py
   ```

### 代码检查

建议在提交前运行：

```bash
# 代码格式化
black .

# 代码质量检查
flake8 .

# 类型检查
mypy .
```

## 🏗️ 项目结构

```
mcp-metaso/
├── server.py              # 主服务器实现
├── config.py              # 配置管理
├── test_all_scopes.py     # 功能测试
├── requirements.txt       # 生产依赖
├── setup.py              # 包配置
├── README.md             # 项目说明
├── CONTRIBUTING.md       # 贡献指南
├── CHANGELOG.md          # 变更日志
├── LICENSE               # 许可证
└── .gitignore           # Git 忽略规则
```

## 🎯 贡献想法

如果您想贡献但不知道从哪开始，这里有一些想法：

### 功能增强
- 添加更多搜索 scope 类型
- 改进错误处理和用户反馈
- 添加缓存机制提升性能
- 支持更多输出格式

### 工程改进
- 添加更全面的测试套件
- 改进日志记录
- 添加性能监控
- Docker 容器化支持

### 文档改进
- 添加更多使用示例
- 改进 API 文档
- 添加故障排除指南
- 多语言文档支持

## 💡 获取帮助

如果您在贡献过程中遇到问题：

1. 查阅现有的 [Issues](https://github.com/your-username/mcp-metaso/issues)
2. 查看 [README](README.md) 和项目文档
3. 创建新的 Issue 寻求帮助

## 📄 许可证

通过向本项目贡献代码，您同意您的贡献将在 [MIT 许可证](LICENSE) 下授权。

---

再次感谢您的贡献！🎉 
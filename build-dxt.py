#!/usr/bin/env python3
"""
MCP Metaso DXT扩展打包脚本
构建Claude Desktop可双击安装的.dxt扩展文件
"""

import os
import sys
import json
import zipfile
import shutil
from pathlib import Path
from datetime import datetime

def create_icon():
    """创建简单的图标文件（placeholder）"""
    icon_path = Path("icon.png")
    if not icon_path.exists():
        print("📷 创建扩展图标...")
        # 这里创建一个基本的图标占位符
        # 在实际项目中，您应该提供一个真实的PNG图标
        try:
            from PIL import Image, ImageDraw, ImageFont
            
            # 创建64x64的图标
            img = Image.new('RGBA', (64, 64), (0, 123, 255, 255))
            draw = ImageDraw.Draw(img)
            
            # 绘制"M"字母
            try:
                font = ImageFont.truetype("arial.ttf", 40)
            except:
                font = ImageFont.load_default()
            
            # 计算文本位置使其居中
            bbox = draw.textbbox((0, 0), "M", font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = (64 - text_width) // 2
            y = (64 - text_height) // 2
            
            draw.text((x, y), "M", fill="white", font=font)
            img.save(icon_path)
            print(f"✅ 已创建图标: {icon_path}")
            
        except ImportError:
            # 如果没有PIL，创建一个简单的文本文件作为占位符
            print("⚠️ 未安装PIL，创建图标占位符")
            icon_path.write_text("PNG Icon Placeholder - 请替换为真实的64x64 PNG图标")
    else:
        print(f"✅ 使用现有图标: {icon_path}")

def validate_manifest():
    """验证manifest.json文件"""
    manifest_path = Path("manifest.json")
    if not manifest_path.exists():
        print("❌ 未找到manifest.json文件")
        return False
    
    try:
        with open(manifest_path, 'r', encoding='utf-8') as f:
            manifest = json.load(f)
        
        required_fields = ['name', 'version', 'description', 'author', 'server', 'dxt_version']
        for field in required_fields:
            if field not in manifest:
                print(f"❌ manifest.json缺少必需字段: {field}")
                return False
        
        print("✅ manifest.json验证通过")
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ manifest.json格式错误: {e}")
        return False

def create_dxt_package():
    """创建DXT扩展包"""
    print("🔨 开始构建DXT扩展包...")
    
    # 验证必需文件
    if not validate_manifest():
        return False
    
    # 创建图标
    create_icon()
    
    # 准备打包文件列表
    files_to_include = [
        'manifest.json',
        'server.py',
        'config.py', 
        'requirements.txt',
        'icon.png',
        'README.md',
        'LICENSE'
    ]
    
    # 可选文件
    optional_files = [
        'CHANGELOG.md',
        'test_all_scopes.py'
    ]
    
    # 检查文件是否存在
    missing_files = []
    for file_path in files_to_include:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ 缺少必需文件: {', '.join(missing_files)}")
        return False
    
    # 添加存在的可选文件
    for file_path in optional_files:
        if Path(file_path).exists():
            files_to_include.append(file_path)
    
    # 读取版本信息
    with open('manifest.json', 'r', encoding='utf-8') as f:
        manifest = json.load(f)
    
    version = manifest['version']
    package_name = f"mcp-metaso-{version}.dxt"
    
    print(f"📦 创建DXT包: {package_name}")
    
    # 创建ZIP文件（DXT本质上是ZIP文件）
    with zipfile.ZipFile(package_name, 'w', zipfile.ZIP_DEFLATED) as dxt_file:
        for file_path in files_to_include:
            print(f"   添加文件: {file_path}")
            dxt_file.write(file_path, file_path)
        
        # 添加构建信息
        build_info = {
            "build_time": datetime.now().isoformat(),
            "build_version": version,
            "files_included": files_to_include
        }
        
        dxt_file.writestr("build_info.json", 
                         json.dumps(build_info, indent=2, ensure_ascii=False))
    
    print(f"🎉 DXT扩展包构建完成: {package_name}")
    print(f"📁 文件大小: {Path(package_name).stat().st_size / 1024:.1f} KB")
    
    return True

def create_installation_guide():
    """创建安装指南"""
    guide_content = f"""# MCP Metaso DXT扩展安装指南

## 什么是DXT扩展？

DXT（Desktop Extension）是Claude Desktop的扩展格式，允许您通过双击安装MCP服务器，就像安装浏览器扩展一样简单。

## 安装步骤

1. **下载扩展文件**
   - 下载 `mcp-metaso-{Path('manifest.json').exists() and json.loads(Path('manifest.json').read_text())['version'] or '1.1.0'}.dxt` 文件到您的计算机

2. **安装扩展**
   - 打开Claude Desktop应用
   - 导航到 **设置 > 扩展**
   - 点击"从.dxt文件安装"
   - 选择下载的.dxt文件
   - 点击"安装"

3. **配置API密钥**
   - 扩展安装后，系统会提示您配置Metaso API密钥
   - 前往 [https://metaso.cn](https://metaso.cn) 获取您的API密钥
   - 在配置界面中输入API密钥
   - 点击"保存"完成配置

4. **开始使用**
   - 重启Claude Desktop（如果需要）
   - 在对话中，您现在可以使用以下工具：
     - **metaso_search**: 多维搜索（网页、学术、图片等）
     - **metaso_reader**: 网页内容解析

## 使用示例

安装完成后，您可以向Claude发送如下请求：

- "搜索人工智能的最新发展"
- "使用学术搜索查找机器学习论文"  
- "解析这个网页的内容: https://example.com"

## 故障排除

### 扩展无法安装
- 确保您运行的是最新版本的Claude Desktop
- 检查.dxt文件是否完整下载
- 验证您有足够的磁盘空间

### 工具不可用
- 重启Claude Desktop
- 检查API密钥配置是否正确
- 在设置中验证扩展状态

### 搜索失败
- 确认API密钥有效且未过期
- 检查网络连接
- 查看扩展日志获取详细错误信息

## 支持

如果您遇到问题，请：
1. 查看扩展设置中的日志信息
2. 访问项目GitHub页面报告问题
3. 确保您使用的是最新版本的扩展

---

## 开发者信息

- **扩展名称**: MCP Metaso搜索引擎
- **版本**: {Path('manifest.json').exists() and json.loads(Path('manifest.json').read_text())['version'] or '1.1.0'}
- **许可证**: MIT
- **源代码**: https://github.com/HundunOnline/mcp-metaso

构建时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    guide_path = Path("DXT安装指南.md")
    guide_path.write_text(guide_content, encoding='utf-8')
    print(f"📖 已创建安装指南: {guide_path}")

def main():
    """主函数"""
    print("🚀 MCP Metaso DXT扩展构建器")
    print("=" * 50)
    
    # 检查当前目录
    required_files = ['manifest.json', 'server.py', 'requirements.txt']
    for file_path in required_files:
        if not Path(file_path).exists():
            print(f"❌ 当前目录缺少必需文件: {file_path}")
            print("请在mcp-metaso项目根目录运行此脚本")
            sys.exit(1)
    
    try:
        # 构建DXT包
        if create_dxt_package():
            # 创建安装指南
            create_installation_guide()
            
            print("\n🎉 构建完成！")
            print("\n📋 后续步骤:")
            print("1. 测试.dxt文件的安装")
            print("2. 上传到发布页面供用户下载")
            print("3. 考虑提交到Claude扩展目录")
            
        else:
            print("\n❌ 构建失败")
            sys.exit(1)
            
    except Exception as e:
        print(f"\n❌ 构建过程中出错: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
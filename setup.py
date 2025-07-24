"""Setup script for MCP Metaso Server"""
from setuptools import setup, find_packages

# 读取README文件内容作为长描述
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# 读取requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh.readlines() if line.strip() and not line.startswith("#")]

setup(
    name="mcp-metaso",
    version="1.0.0",
    description="MCP server for Metaso AI search engine with multi-scope search support using FastMCP SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="MCP Metaso Contributors",
    author_email="", 
    url="https://github.com/HundunOnline/mcp-metaso",
    project_urls={
        "Bug Reports": "https://github.com/HundunOnline/mcp-metaso/issues",
        "Source": "https://github.com/HundunOnline/mcp-metaso",
        "Documentation": "https://github.com/HundunOnline/mcp-metaso#readme",
    },
    packages=find_packages(exclude=["tests*"]),
    py_modules=["server", "config"],
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "mcp-metaso=server:main",
        ],
    },
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: Markdown",
        "Framework :: AsyncIO",
    ],
    keywords="mcp metaso search ai fastmcp claude desktop protocol",
    license="MIT",
    zip_safe=False,
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.yml", "*.yaml"],
    },
)
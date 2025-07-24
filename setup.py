"""Setup script for MCP Metaso Server"""
from setuptools import setup, find_packages

setup(
    name="mcp-metaso",
    version="0.4.0",
    description="MCP server for Metaso AI search engine with multi-scope search support using FastMCP SDK",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    py_modules=["server", "config"],
    install_requires=[
        "mcp>=1.1.0",
        "httpx>=0.27.0",
    ],
    entry_points={
        "console_scripts": [
            "mcp-metaso=server:main",
        ],
    },
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
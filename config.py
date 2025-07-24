"""MCP Metaso Server配置管理"""
import os
from typing import Optional


class Config:
    """配置类"""
    
    def __init__(self):
        self.api_key = self._get_optional_env("METASO_API_KEY", "")
        self.base_url = "https://metaso.cn/api/v1"
        self.timeout = 30
        
    def _get_required_env(self, key: str) -> str:
        """获取必需的环境变量"""
        value = os.getenv(key)
        if not value:
            raise ValueError(f"环境变量 {key} 是必需的，请设置后重试")
        return value
    
    def _get_optional_env(self, key: str, default: str) -> str:
        """获取可选的环境变量"""
        return os.getenv(key, default)


# 全局配置实例
config = Config()
#!/usr/bin/env python3
"""MCP Metaso服务器 - 使用官方FastMCP SDK实现"""
import asyncio
import logging
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
from config import config

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 创建FastMCP服务器实例
mcp = FastMCP("mcp-metaso")

# 定义scope到结果key的映射
SCOPE_RESULT_MAPPING = {
    "webpage": "webpages",
    "document": "documents", 
    "scholar": "scholars",
    "image": "images",
    "video": "videos",
    "podcast": "podcasts"
}


def format_webpage_result(item: dict, index: int) -> str:
    """格式化网页搜索结果"""
    formatted = f"## 结果 {index}\n"
    formatted += f"**标题**: {item.get('title', 'N/A')}\n"
    formatted += f"**URL**: {item.get('link', 'N/A')}\n"
    formatted += f"**摘要**: {item.get('snippet', 'N/A')}\n"
    
    if item.get('displayDate'):
        formatted += f"**发布时间**: {item['displayDate']}\n"
    
    return formatted + "\n"


def format_document_result(item: dict, index: int) -> str:
    """格式化文库搜索结果"""
    formatted = f"## 文库结果 {index}\n"
    formatted += f"**标题**: {item.get('title', 'N/A')}\n"
    
    # 处理作者信息 - 可能是数组或字符串
    authors = item.get('authors', item.get('author', 'N/A'))
    if isinstance(authors, list):
        authors_str = ', '.join(authors)
    else:
        authors_str = str(authors) if authors != 'N/A' else 'N/A'
    formatted += f"**作者/来源**: {authors_str}\n"
    
    formatted += f"**文档链接**: {item.get('link', item.get('url', 'N/A'))}\n"
    formatted += f"**摘要**: {item.get('snippet', item.get('abstract', 'N/A'))}\n"
    
    # 显示相关度和位置信息
    if item.get('score'):
        formatted += f"**相关度**: {item['score']}\n"
    if item.get('position'):
        formatted += f"**排序位置**: {item['position']}\n"
    
    # 兼容其他可能的字段
    if item.get('source'):
        formatted += f"**文档来源**: {item['source']}\n"
    if item.get('publishDate'):
        formatted += f"**发布时间**: {item['publishDate']}\n"
    
    return formatted + "\n"


def format_scholar_result(item: dict, index: int) -> str:
    """格式化学术搜索结果"""
    formatted = f"## 学术结果 {index}\n"
    formatted += f"**标题**: {item.get('title', 'N/A')}\n"
    
    # 处理作者信息 - 可能是数组或字符串
    authors = item.get('authors', item.get('author', 'N/A'))
    if isinstance(authors, list):
        authors_str = ', '.join(authors)
    else:
        authors_str = str(authors) if authors != 'N/A' else 'N/A'
    formatted += f"**作者**: {authors_str}\n"
    
    formatted += f"**URL**: {item.get('link', item.get('url', 'N/A'))}\n"
    formatted += f"**摘要**: {item.get('snippet', item.get('abstract', 'N/A'))}\n"
    
    # 显示发表日期
    if item.get('date'):
        formatted += f"**发表日期**: {item['date']}\n"
    elif item.get('year'):
        formatted += f"**发表年份**: {item['year']}\n"
    
    # 显示相关度和位置信息
    if item.get('score'):
        formatted += f"**相关度**: {item['score']}\n"
    if item.get('position'):
        formatted += f"**排序位置**: {item['position']}\n"
    
    # 显示期刊/会议信息
    if item.get('venue', item.get('journal')):
        formatted += f"**期刊/会议**: {item.get('venue', item.get('journal'))}\n"
    
    # 显示引用和DOI信息
    if item.get('citationCount'):
        formatted += f"**引用次数**: {item['citationCount']}\n"
    if item.get('doi'):
        formatted += f"**DOI**: {item['doi']}\n"
    
    return formatted + "\n"


def format_image_result(item: dict, index: int) -> str:
    """格式化图片搜索结果"""
    formatted = f"## 图片结果 {index}\n"
    formatted += f"**标题**: {item.get('title', 'N/A')}\n"
    formatted += f"**图片URL**: {item.get('imageUrl', 'N/A')}\n"
    
    # 显示图片尺寸信息
    if item.get('imageWidth') and item.get('imageHeight'):
        formatted += f"**尺寸**: {item['imageWidth']} x {item['imageHeight']}\n"
    
    # 显示评分和位置信息
    if item.get('score'):
        formatted += f"**相关度**: {item['score']}\n"
    if item.get('position'):
        formatted += f"**排序位置**: {item['position']}\n"
    
    # 兼容其他可能的字段
    if item.get('sourceUrl', item.get('link')):
        formatted += f"**来源页面**: {item.get('sourceUrl', item.get('link'))}\n"
    if item.get('description'):
        formatted += f"**描述**: {item['description']}\n"
    
    return formatted + "\n"


def format_video_result(item: dict, index: int) -> str:
    """格式化视频搜索结果"""
    formatted = f"## 视频结果 {index}\n"
    formatted += f"**标题**: {item.get('title', 'N/A')}\n"
    
    # 处理作者/频道信息 - 可能是数组或字符串
    authors = item.get('authors', item.get('channel', 'N/A'))
    if isinstance(authors, list):
        authors_str = ', '.join(authors)
    else:
        authors_str = str(authors) if authors != 'N/A' else 'N/A'
    formatted += f"**创作者/频道**: {authors_str}\n"
    
    formatted += f"**视频链接**: {item.get('link', item.get('url', 'N/A'))}\n"
    formatted += f"**描述**: {item.get('snippet', item.get('description', 'N/A'))}\n"
    
    # 显示时长信息
    if item.get('duration'):
        try:
            duration_sec = int(item['duration'])
            minutes = duration_sec // 60
            seconds = duration_sec % 60
            formatted += f"**时长**: {minutes}分{seconds}秒 ({duration_sec}秒)\n"
        except (ValueError, TypeError):
            formatted += f"**时长**: {item['duration']}\n"
    
    # 显示发布时间
    if item.get('date'):
        formatted += f"**发布时间**: {item['date']}\n"
    elif item.get('publishDate'):
        formatted += f"**发布时间**: {item['publishDate']}\n"
    
    # 显示相关度和位置信息
    if item.get('score'):
        formatted += f"**相关度**: {item['score']}\n"
    if item.get('position'):
        formatted += f"**排序位置**: {item['position']}\n"
    
    # 显示封面图片
    if item.get('coverImage'):
        formatted += f"**封面图片**: {item['coverImage']}\n"
    elif item.get('thumbnail'):
        formatted += f"**缩略图**: {item['thumbnail']}\n"
    
    # 兼容其他字段
    if item.get('viewCount'):
        formatted += f"**观看次数**: {item['viewCount']}\n"
    
    return formatted + "\n"


def format_podcast_result(item: dict, index: int) -> str:
    """格式化播客搜索结果"""
    formatted = f"## 播客结果 {index}\n"
    formatted += f"**标题**: {item.get('title', 'N/A')}\n"
    
    # 处理作者/主持人信息 - 可能是数组或字符串
    authors = item.get('authors', item.get('host', 'N/A'))
    if isinstance(authors, list):
        authors_str = ', '.join(authors)
    else:
        authors_str = str(authors) if authors != 'N/A' else 'N/A'
    formatted += f"**主持人/嘉宾**: {authors_str}\n"
    
    formatted += f"**播客链接**: {item.get('link', item.get('url', 'N/A'))}\n"
    formatted += f"**内容简介**: {item.get('snippet', item.get('description', 'N/A'))}\n"
    
    # 显示时长信息
    if item.get('duration'):
        try:
            duration_sec = int(item['duration'])
            hours = duration_sec // 3600
            minutes = (duration_sec % 3600) // 60
            seconds = duration_sec % 60
            if hours > 0:
                formatted += f"**时长**: {hours}小时{minutes}分{seconds}秒 ({duration_sec}秒)\n"
            else:
                formatted += f"**时长**: {minutes}分{seconds}秒 ({duration_sec}秒)\n"
        except (ValueError, TypeError):
            formatted += f"**时长**: {item['duration']}\n"
    
    # 显示发布时间
    if item.get('date'):
        formatted += f"**发布时间**: {item['date']}\n"
    elif item.get('publishDate'):
        formatted += f"**发布时间**: {item['publishDate']}\n"
    
    # 显示相关度和位置信息
    if item.get('score'):
        formatted += f"**相关度**: {item['score']}\n"
    if item.get('position'):
        formatted += f"**排序位置**: {item['position']}\n"
    
    # 兼容其他字段
    if item.get('podcastName', item.get('show')):
        formatted += f"**播客节目**: {item.get('podcastName', item.get('show'))}\n"
    if item.get('audioUrl'):
        formatted += f"**音频链接**: {item['audioUrl']}\n"
    
    return formatted + "\n"


# 格式化函数映射
RESULT_FORMATTERS = {
    "webpage": format_webpage_result,
    "document": format_document_result,
    "scholar": format_scholar_result, 
    "image": format_image_result,
    "video": format_video_result,
    "podcast": format_podcast_result
}


@mcp.tool()
async def metaso_search(
    query: str, 
    scope: str = "webpage", 
    include_summary: bool = False, 
    size: int = 10
) -> str:
    """使用Metaso AI搜索引擎搜索信息
    
    Args:
        query: 搜索查询词
        scope: 搜索范围，支持：webpage（网页）、document（文库）、scholar（学术）、image（图片）、video（视频）、podcast（播客）
        include_summary: 是否包含摘要，默认False
        size: 返回结果数量，默认10，范围1-20
    """
    try:
        # 验证scope参数
        if scope not in SCOPE_RESULT_MAPPING:
            supported_scopes = ", ".join(SCOPE_RESULT_MAPPING.keys())
            return f"错误: 不支持的搜索范围 '{scope}'。支持的范围: {supported_scopes}"
        
        url = f"{config.base_url}/search"
        headers = {
            "Authorization": f"Bearer {config.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        data = {
            "q": query,
            "scope": scope,
            "includeSummary": include_summary,
            "size": str(size)
        }
        
        async with httpx.AsyncClient(timeout=config.timeout) as client:
            response = await client.post(url, headers=headers, json=data)
            response.raise_for_status()
            result = response.json()
        
        # 格式化搜索结果
        scope_cn_mapping = {
            "webpage": "网页",
            "document": "文库", 
            "scholar": "学术",
            "image": "图片",
            "video": "视频",
            "podcast": "播客"
        }
        
        formatted_result = f"# {scope_cn_mapping[scope]}搜索结果：{query}\n\n"
        
        # 处理摘要
        if include_summary and result.get('summary'):
            formatted_result += f"## 搜索摘要\n{result['summary']}\n\n"
        
        # 获取对应scope的结果数据
        result_key = SCOPE_RESULT_MAPPING[scope]
        items = result.get(result_key, [])
        
        if not items:
            formatted_result += f"未找到相关{scope_cn_mapping[scope]}结果。\n"
            return formatted_result
        
        # 使用对应的格式化函数
        formatter = RESULT_FORMATTERS[scope]
        for i, item in enumerate(items, 1):
            formatted_result += formatter(item, i)
        
        # 添加结果统计
        formatted_result += f"---\n**共找到 {len(items)} 条{scope_cn_mapping[scope]}结果**"
        
        return formatted_result
        
    except httpx.HTTPError as e:
        logger.error(f"HTTP请求错误: {e}")
        return f"搜索失败: HTTP错误 - {str(e)}"
    except Exception as e:
        logger.error(f"搜索失败: {e}")
        return f"搜索失败: {str(e)}"


@mcp.tool()
async def metaso_reader(url: str, output_format: str = "markdown") -> str:
    """解析网页内容并提取文本
    
    Args:
        url: 要解析的网页URL
        output_format: 输出格式，支持"markdown"（默认）或"json"
    """
    try:
        api_url = f"{config.base_url}/reader"
        headers = {
            "Authorization": f"Bearer {config.api_key}",
            "Content-Type": "application/json",
            "Accept": "text/plain" if output_format == "markdown" else "application/json"
        }
        data = {"url": url}
        
        async with httpx.AsyncClient(timeout=config.timeout) as client:
            response = await client.post(api_url, headers=headers, json=data)
            response.raise_for_status()
        
        if output_format == "markdown":
            content = response.text
        else:
            import json
            content = json.dumps(response.json(), ensure_ascii=False, indent=2)
        
        formatted_content = f"# 网页内容解析\n\n**URL**: {url}\n\n## 解析结果\n\n{content}"
        return formatted_content
        
    except httpx.HTTPError as e:
        logger.error(f"HTTP请求错误: {e}")
        return f"网页解析失败: HTTP错误 - {str(e)}"
    except Exception as e:
        logger.error(f"网页解析失败: {e}")
        return f"网页解析失败: {str(e)}"


def main():
    """主函数"""
    logger.info("启动MCP Metaso服务器...")
    
    # 检查API密钥
    if not config.api_key:
        logger.error("错误: 未设置METASO_API_KEY环境变量")
        logger.error("请使用: export METASO_API_KEY='your_key_here'")
        return
    
    # 使用FastMCP的run方法启动服务器
    mcp.run()


if __name__ == "__main__":
    main() 
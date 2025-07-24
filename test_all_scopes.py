#!/usr/bin/env python3
"""MCP Metaso服务器全面测试脚本 - 测试所有scope功能"""
import asyncio
import sys
from server import metaso_search, metaso_reader

# 测试用例定义
TEST_CASES = [
    {
        "scope": "webpage",
        "query": "人工智能最新发展",
        "description": "测试网页搜索"
    },
    {
        "scope": "document", 
        "query": "机器学习算法",
        "description": "测试文库搜索"
    },
    {
        "scope": "scholar",
        "query": "deep learning transformer",
        "description": "测试学术搜索"
    },
    {
        "scope": "image",
        "query": "猫咪",
        "description": "测试图片搜索"
    },
    {
        "scope": "video",
        "query": "编程教程",
        "description": "测试视频搜索"
    },
    {
        "scope": "podcast",
        "query": "科技播客",
        "description": "测试播客搜索"
    }
]


async def test_scope(scope: str, query: str, description: str) -> bool:
    """测试特定scope的搜索功能"""
    print(f"\n{'='*60}")
    print(f"{description} (scope: {scope})")
    print(f"查询: {query}")
    print(f"{'='*60}")
    
    try:
        result = await metaso_search(
            query=query,
            scope=scope,
            include_summary=False,  # 暂时不包含摘要以简化测试
            size=3  # 限制结果数量以便快速测试
        )
        
        print("✅ 搜索成功")
        print("结果预览:")
        print(result[:800] + "..." if len(result) > 800 else result)
        print(f"\n结果长度: {len(result)} 字符")
        return True
        
    except Exception as e:
        print(f"❌ 搜索失败: {e}")
        return False


async def test_invalid_scope():
    """测试无效scope的错误处理"""
    print(f"\n{'='*60}")
    print("测试无效scope错误处理")
    print(f"{'='*60}")
    
    try:
        result = await metaso_search(
            query="测试查询",
            scope="invalid_scope",
            size=1
        )
        
        if "错误: 不支持的搜索范围" in result:
            print("✅ 无效scope错误处理正确")
            print(f"错误信息: {result}")
            return True
        else:
            print("❌ 无效scope错误处理失败")
            print(f"意外结果: {result}")
            return False
            
    except Exception as e:
        print(f"❌ 测试异常: {e}")
        return False


async def test_with_summary():
    """测试带摘要的搜索"""
    print(f"\n{'='*60}")
    print("测试带摘要的网页搜索")
    print(f"{'='*60}")
    
    try:
        result = await metaso_search(
            query="2024年AI发展趋势",
            scope="webpage",
            include_summary=True,
            size=2
        )
        
        print("✅ 带摘要搜索成功")
        if "搜索摘要" in result:
            print("✅ 成功包含搜索摘要")
        else:
            print("⚠️  未检测到搜索摘要（可能API未返回摘要）")
        
        print("结果预览:")
        print(result[:800] + "..." if len(result) > 800 else result)
        return True
        
    except Exception as e:
        print(f"❌ 带摘要搜索失败: {e}")
        return False


async def test_reader_function():
    """测试网页解析功能"""
    print(f"\n{'='*60}")
    print("测试网页解析功能")
    print(f"{'='*60}")
    
    try:
        result = await metaso_reader("https://www.baidu.com")
        print("✅ 网页解析成功")
        print("解析结果预览:")
        print(result[:400] + "..." if len(result) > 400 else result)
        return True
        
    except Exception as e:
        print(f"❌ 网页解析失败: {e}")
        return False


async def main():
    """主测试函数"""
    print("🚀 开始MCP Metaso服务器全面功能测试")
    print(f"测试时间: {asyncio.get_event_loop().time()}")
    
    # 检查环境变量
    from config import config
    if not config.api_key:
        print("❌ 未设置METASO_API_KEY环境变量")
        print("请使用: export METASO_API_KEY='your_key_here'")
        sys.exit(1)
    
    print(f"✅ API密钥已配置 (长度: {len(config.api_key)} 字符)")
    
    # 测试结果统计
    test_results = {
        "scope_tests": [],
        "invalid_scope": False,
        "summary_test": False,
        "reader_test": False
    }
    
    # 测试所有scope
    print(f"\n📋 开始测试 {len(TEST_CASES)} 种不同的搜索scope...")
    
    for test_case in TEST_CASES:
        success = await test_scope(
            scope=test_case["scope"],
            query=test_case["query"], 
            description=test_case["description"]
        )
        test_results["scope_tests"].append({
            "scope": test_case["scope"],
            "success": success,
            "description": test_case["description"]
        })
        
        # 短暂延迟避免频繁请求
        await asyncio.sleep(1)
    
    # 测试错误处理
    print(f"\n🔍 测试错误处理...")
    test_results["invalid_scope"] = await test_invalid_scope()
    
    # 测试摘要功能
    print(f"\n📝 测试摘要功能...")
    test_results["summary_test"] = await test_with_summary()
    
    # 测试网页解析功能
    print(f"\n🌐 测试网页解析功能...")
    test_results["reader_test"] = await test_reader_function()
    
    # 输出测试总结
    print(f"\n{'='*80}")
    print("📊 测试总结报告")
    print(f"{'='*80}")
    
    print("\n🎯 Scope搜索测试结果:")
    successful_scopes = 0
    for result in test_results["scope_tests"]:
        status = "✅ 通过" if result["success"] else "❌ 失败"
        print(f"  {result['scope']:>10}: {status} - {result['description']}")
        if result["success"]:
            successful_scopes += 1
    
    print(f"\n📈 测试统计:")
    print(f"  Scope测试: {successful_scopes}/{len(TEST_CASES)} 通过")
    print(f"  错误处理: {'✅ 通过' if test_results['invalid_scope'] else '❌ 失败'}")
    print(f"  摘要功能: {'✅ 通过' if test_results['summary_test'] else '❌ 失败'}")
    print(f"  网页解析: {'✅ 通过' if test_results['reader_test'] else '❌ 失败'}")
    
    # 计算总成功率
    total_tests = len(TEST_CASES) + 3  # scope测试 + 3个额外测试
    passed_tests = successful_scopes + sum([
        test_results["invalid_scope"],
        test_results["summary_test"],
        test_results["reader_test"]
    ])
    
    success_rate = (passed_tests / total_tests) * 100
    print(f"\n🎉 总体成功率: {passed_tests}/{total_tests} ({success_rate:.1f}%)")
    
    if success_rate >= 80:
        print("🎊 恭喜！服务器功能测试表现优秀！")
        return 0
    elif success_rate >= 60:
        print("👍 服务器基本功能正常，部分功能需要调优。")
        return 0
    else:
        print("⚠️  服务器存在较多问题，请检查配置和网络连接。")
        return 1


if __name__ == "__main__":
    try:
        exit_code = asyncio.run(main())
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n⏹️  测试被用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 测试过程中发生严重错误: {e}")
        sys.exit(1) 
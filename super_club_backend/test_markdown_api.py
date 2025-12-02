#!/usr/bin/env python3
"""
简单的 API 测试脚本：测试 Markdown 文件读取功能
"""
import os
from pathlib import Path

def test_read_markdown_file():
    """测试读取 Markdown 文件"""
    # 测试文件路径
    test_file = Path(__file__).parent / "articles" / "test-article.md"
    
    print("🧪 测试 Markdown 文件读取功能")
    print("-" * 50)
    print(f"📁 测试文件路径: {test_file}")
    print(f"📁 文件是否存在: {test_file.exists()}")
    
    if not test_file.exists():
        print("❌ 测试文件不存在！")
        return False
    
    try:
        # 读取文件内容
        with open(test_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"✅ 文件读取成功！")
        print(f"📊 文件大小: {len(content)} 字符")
        print(f"📊 行数: {len(content.splitlines())} 行")
        print("\n📝 文件内容预览（前 200 字符）:")
        print("-" * 50)
        print(content[:200] + "...")
        print("-" * 50)
        
        # 检查 Markdown 语法
        has_headings = "#" in content
        has_code = "```" in content
        has_list = "-" in content or "*" in content
        has_table = "|" in content
        
        print("\n📋 Markdown 语法检查:")
        print(f"  {'✅' if has_headings else '❌'} 标题 (#)")
        print(f"  {'✅' if has_code else '❌'} 代码块 (```)")
        print(f"  {'✅' if has_list else '❌'} 列表 (-/*)")
        print(f"  {'✅' if has_table else '❌'} 表格 (|)")
        
        return True
        
    except Exception as e:
        print(f"❌ 读取文件失败: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_file_path_logic():
    """测试文件路径逻辑"""
    print("\n🧪 测试文件路径解析逻辑")
    print("-" * 50)
    
    # 模拟后端代码逻辑
    def read_markdown_file(file_path: str):
        """从文件系统读取 markdown 文件内容"""
        try:
            if not os.path.isabs(file_path):
                # 获取项目根目录（super_club_backend）
                base_dir = Path(__file__).parent
                file_path = base_dir / file_path
            else:
                file_path = Path(file_path)
            
            if file_path.exists() and file_path.suffix.lower() in ['.md', '.markdown']:
                with open(file_path, 'r', encoding='utf-8') as f:
                    return f.read()
            return None
        except Exception as e:
            print(f"错误: {e}")
            return None
    
    # 测试相对路径
    test_path = "articles/test-article.md"
    print(f"📁 测试相对路径: {test_path}")
    content = read_markdown_file(test_path)
    if content:
        print(f"✅ 相对路径读取成功！内容长度: {len(content)} 字符")
    else:
        print("❌ 相对路径读取失败！")
    
    # 测试绝对路径
    abs_path = str(Path(__file__).parent / "articles" / "test-article.md")
    print(f"\n📁 测试绝对路径: {abs_path}")
    content = read_markdown_file(abs_path)
    if content:
        print(f"✅ 绝对路径读取成功！内容长度: {len(content)} 字符")
    else:
        print("❌ 绝对路径读取失败！")

if __name__ == "__main__":
    print("=" * 50)
    print("🚀 Markdown 文件读取功能测试")
    print("=" * 50)
    
    success = test_read_markdown_file()
    test_file_path_logic()
    
    print("\n" + "=" * 50)
    if success:
        print("✅ 测试完成！文件读取功能正常。")
        print("\n💡 下一步:")
        print("   1. 启动后端服务: cd super_club_backend && python3 run.py")
        print("   2. 启动前端服务: cd super_club && npm run dev")
        print("   3. 访问文章详情页测试 Markdown 渲染")
    else:
        print("❌ 测试失败！请检查文件路径和权限。")
    print("=" * 50)


#!/usr/bin/env python3
"""
更新模型文件以适配MySQL数据库
"""
import os
import re

def update_model_file(file_path):
    """更新单个模型文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替换导入语句
    content = re.sub(
        r'from sqlalchemy.dialects.postgresql import UUID, ARRAY, JSONB',
        'from sqlalchemy.dialects.mysql import JSON',
        content
    )
    content = re.sub(
        r'from sqlalchemy.dialects.postgresql import UUID, ARRAY',
        '',
        content
    )
    content = re.sub(
        r'from sqlalchemy.dialects.postgresql import UUID',
        '',
        content
    )
    
    # 替换UUID字段
    content = re.sub(
        r'Column\(UUID\(as_uuid=True\), primary_key=True, default=uuid\.uuid4\)',
        'Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))',
        content
    )
    content = re.sub(
        r'Column\(UUID\(as_uuid=True\), ForeignKey\("([^"]+)"\)([^)]*)\)',
        r'Column(String(36), ForeignKey("\1")\2)',
        content
    )
    content = re.sub(
        r'Column\(UUID\(as_uuid=True\)([^)]*)\)',
        r'Column(String(36)\1)',
        content
    )
    
    # 替换ARRAY字段为TEXT (JSON字符串)
    content = re.sub(
        r'Column\(ARRAY\(String\)([^)]*)\)',
        r'Column(TEXT\1)',
        content
    )
    
    # 替换JSONB字段为JSON
    content = re.sub(
        r'Column\(JSONB([^)]*)\)',
        r'Column(JSON\1)',
        content
    )
    
    # 清理多余的空行
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated: {file_path}")

def main():
    """主函数"""
    models_dir = "app/models"
    
    # 获取所有Python模型文件
    for filename in os.listdir(models_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            file_path = os.path.join(models_dir, filename)
            update_model_file(file_path)
    
    print("All model files updated for MySQL compatibility!")

if __name__ == "__main__":
    main()

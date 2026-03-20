# 语雀文档导出工具

一个用于导出语雀知识库文档的 Python 工具，支持按知识库分类保存。

## 功能特性

- 获取用户所有语雀知识库列表
- 导出 Doc 类型文档为 Markdown 格式
- 导出 Sheet 类型文档为 Excel 格式
- 自动按知识库名称创建文件夹结构
- 支持异步导出（Sheet 文档）

## 文件夹结构

```
exported_docs/
├── @2024 For Working/
│   ├── Doc文档/
│   └── Sheet表格/
├── @2024 For Power/
│   ├── Doc文档/
│   └── Sheet表格/
├── @2026/
│   ├── Doc文档/
│   └── Sheet表格/
└── BackUp/
    ├── Doc文档/
    └── Sheet表格/
```

## 使用方法

1. 安装依赖：
```bash
pip install requests
```

2. 更新脚本中的 Cookie：
   - 登录语雀网页
   - 打开浏览器开发者工具 -> Network
   - 找到任意一个 API 请求，复制 Cookie 头
   - 替换脚本中的 `self.cookie` 值

3. 运行脚本：
```bash
python export_yuque.py
```

## 配置说明

在 `main()` 函数中可以修改：
- `OUTPUT_DIR`: 导出文件保存目录
- `export_markdown`: 是否导出 Markdown
- `export_pdf`: 是否导出 PDF（默认关闭）

## 注意事项

- Cookie 有效期有限，如遇导出失败请更新 Cookie
- PDF 导出需要异步等待，语雀 API 不支持查询导出状态
- 部分文档类型（如 Table）暂不支持导出

## 依赖

- Python 3.7+
- requests

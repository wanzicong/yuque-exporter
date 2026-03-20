#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
语雀文档导出工具
支持导出 Doc 类型文档为 Markdown/PDF，Sheet 类型文档为 Excel
按知识库名称创建文件夹结构
"""

import requests
import json
import os
import time
import sys
from pathlib import Path

# 设置标准输出编码为 UTF-8
sys.stdout.reconfigure(encoding='utf-8', errors='replace')


class YuqueExporter:
    """语雀文档导出器"""

    def __init__(self, output_dir: str = "exported_docs"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # 基础 Headers
        self.base_headers = {
            'Accept': 'application/json',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': 'https://www.yuque.com',
            'Referer': 'https://www.yuque.com/dashboard/books',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Microsoft Edge";v="146"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'x-csrf-token': 'NOiYaCtUfQ2i6ypFVZ0xpeTF',
            'x-login': 'byyourself-dw69k',
        }

        # Cookie (需要更新为最新的)
        self.cookie = 'receive-cookie-deprecation=1; lang=zh-cn; receive-cookie-deprecation=1; _yuque_session=HSEaUzjsLynY3LVnFPaJZAUK6p9qSQlgXIF9y3ziQ4zfsmEWKYqRSQng9-yTpo8vdctWFthg8McBN6SAxOKl2g==; tfstk=g_hxpL0lu3xDyORWvsvkS27FPtYkEL02mmuCslqcC0n-R2S0Ct4011i3qjqmoSTtXDiYIc3wuPZsfcEinLAnuqPa1H4vtB0qHVNuTcebC_1SzPXblL2b60pxuHxHtQ0Q2GjkxqDCCe377uafG-a6yga_VG1jfow5VyUU1lisf8s78yf1C-1jPaZz55Zsf5T-PuzT1li_1U3SGmvY2Eaf6YdRwMHO4f511bUYFL0bVKmKarhaxqGA11_Qk-EIlutbkIA4FVyt_N5TpqMEbyifcnFsyynLJmpG7oHS-jqmJwftlSHo-ze55ePzBoHSG8Q11qVmUcDtDnB4cxm8Lzw5WBzoxugqGYLNVqi3DSa7EBTKPRMogJlDVsFILqVmC0ORMDsy-Xcpzes3vPXXyUBNQ-az4jSocDywI248xEUAQOyGzzEHyUBNQ-azykYAXOWaIa5..; aliyungf_tc=2a7ebdbb35887593bdfc5f488b4690be0b42204bf7b3de61e5024f1ac823d70e; yuque_ctoken=NOiYaCtUfQ2i6ypFVZ0xpeTF; current_theme=default; acw_tc=76b20f9b17739966526343447e009e347767771df132f4c042d54e695cc77a; ssxmod_itna=1-YuDQPUohOiAKi7G7DgDKuFDmx0htiDeq0dGMD3de7t=GcD8OD0pPOoDknKpiiFAAAGu6xbDiut5MD0vepDnqD8XDQeDvKZRYv4MUE0hTo=xrrRYitKnng8obF0EOhPyFFB/RnU18WVq/m7=lS8GrDB3DbqDyF0ioB7eD4R3Dt4DIDAYDDxDWmeGIDGYD7OuiP1TDm44=txGyFCaD08uXCAG=LWatpAG3xiYNdDDltBDsD0AmxYp=P=rDm'

        self.session = requests.Session()
        self.session.headers.update(self.base_headers)
        self.session.cookies.update(self._parse_cookie(self.cookie))

    def get_all_books(self) -> list:
        """获取所有知识库列表"""
        url = "https://www.yuque.com/api/mine/book_stacks"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            data = response.json()

            books = []
            if data.get('data'):
                for stack in data['data']:
                    stack_name = stack.get('name', '默认分组')
                    for book in stack.get('books', []):
                        book['stack_name'] = stack_name
                        books.append(book)

            print(f"获取到 {len(books)} 个知识库")
            return books
        except requests.exceptions.RequestException as e:
            print(f"获取知识库列表失败: {e}")
            return []

    def _parse_cookie(self, cookie_str: str) -> dict:
        """解析 Cookie 字符串"""
        cookie_dict = {}
        for item in cookie_str.split('; '):
            if '=' in item:
                key, value = item.split('=', 1)
                cookie_dict[key.strip()] = value.strip()
        return cookie_dict

    def get_docs_list(self, book_id: str) -> list:
        """获取指定知识库的文档列表"""
        url = f"https://www.yuque.com/api/docs?book_id={book_id}"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            data = response.json()

            if data.get('meta', {}).get('total', -1) == -1:
                docs = data.get('data', [])
                return docs
            return []
        except requests.exceptions.RequestException as e:
            print(f"获取文档列表失败: {e}")
            return []

    def export_doc_markdown(self, doc_id: int, title: str, sub_dir: str = None) -> str:
        """导出 Doc 文档为 Markdown"""
        url = f"https://www.yuque.com/api/docs/{doc_id}/export"

        payload = {
            "type": "markdown",
            "force": 0,
            "options": json.dumps({
                "latexType": 1,
                "enableAnchor": 1,
                "enableBreak": 1,
                "useMdai": 1
            })
        }

        try:
            response = self.session.post(url, json=payload)
            response.raise_for_status()
            result = response.json()

            if result.get('data', {}).get('state') == 'success':
                download_url = result['data']['url']
                return self._download_file(download_url, f"{title}.md", sub_dir)
            else:
                print(f"  [-] 导出失败: {result}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"  [-] 导出 Markdown 失败: {e}")
            return None

    def export_doc_pdf(self, doc_id: int, title: str, sub_dir: str = None) -> str:
        """导出 Doc 文档为 PDF (异步，需要等待)"""
        url = f"https://www.yuque.com/api/docs/{doc_id}/export"

        payload = {
            "type": "pdf",
            "force": 0,
            "options": json.dumps({
                "enableToc": True
            })
        }

        try:
            # 发起导出请求
            response = self.session.post(url, json=payload)
            response.raise_for_status()
            result = response.json()

            # PDF 是异步的，需要等待生成
            if result.get('data', {}).get('state') == 'success':
                # 等待 PDF 生成 (最多等待 30 秒)
                download_url = self._wait_for_export(url, doc_id, 'pdf')
                if download_url:
                    return self._download_file(download_url, f"{title}.pdf", sub_dir)
                else:
                    print(f"  [-] PDF 导出超时")
                    return None
            elif result.get('data', {}).get('state') == 'pending':
                # 等待 PDF 生成
                download_url = self._wait_for_export(url, doc_id, 'pdf')
                if download_url:
                    return self._download_file(download_url, f"{title}.pdf", sub_dir)
                else:
                    print(f"  [-] PDF 导出超时")
                    return None
            else:
                print(f"  [-] 导出失败: {result}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"  [-] 导出 PDF 失败: {e}")
            return None

    def _wait_for_export(self, export_url: str, doc_id: int, export_type: str, max_wait: int = 30) -> str:
        """等待异步导出完成，返回下载 URL"""
        print(f"  [*] 等待 {export_type.upper()} 导出完成...")
        for i in range(max_wait):
            time.sleep(1)
            try:
                # 检查导出状态
                check_url = f"https://www.yuque.com/api/docs/{doc_id}/export"
                response = self.session.get(check_url)
                response.raise_for_status()
                result = response.json()

                if result.get('data', {}).get('state') == 'success':
                    return result['data']['url']
                elif result.get('data', {}).get('state') == 'failed':
                    print(f"  [-] 导出失败")
                    return None

                if (i + 1) % 5 == 0:
                    print(f"  [*] 等待中... ({i + 1}/{max_wait}秒)")

            except requests.exceptions.RequestException as e:
                print(f"  [-] 检查导出状态失败: {e}")
                return None

        return None

    def export_sheet_excel(self, doc_id: int, title: str, sub_dir: str = None) -> str:
        """导出 Sheet 文档为 Excel (异步，需要等待)"""
        url = f"https://www.yuque.com/api/docs/{doc_id}/export"

        payload = {
            "type": "excel",
            "force": 0
        }

        try:
            # 发起导出请求
            response = self.session.post(url, json=payload)
            response.raise_for_status()
            result = response.json()

            # Sheet 是异步的，需要等待生成
            if result.get('data', {}).get('state') == 'success':
                download_url = result['data']['url']
                # 修复 URL 缺少 https:// 的问题
                download_url = self._fix_download_url(download_url)
                return self._download_file(download_url, f"{title}.xlsx", sub_dir)
            elif result.get('data', {}).get('state') == 'pending':
                # 等待 Sheet 生成
                print(f"  [*] 等待 Excel 导出完成...")
                for i in range(30):
                    time.sleep(1)
                    try:
                        check_url = f"https://www.yuque.com/api/docs/{doc_id}/export"
                        response = self.session.get(check_url)
                        response.raise_for_status()
                        result = response.json()

                        if result.get('data', {}).get('state') == 'success':
                            download_url = result['data']['url']
                            download_url = self._fix_download_url(download_url)
                            return self._download_file(download_url, f"{title}.xlsx", sub_dir)
                        elif result.get('data', {}).get('state') == 'failed':
                            print(f"  [-] Excel 导出失败")
                            return None

                        if (i + 1) % 5 == 0:
                            print(f"  [*] 等待中... ({i + 1}/30秒)")

                    except requests.exceptions.RequestException as e:
                        print(f"  [-] 检查导出状态失败: {e}")
                        return None
                print(f"  [-] Excel 导出超时")
                return None
            else:
                print(f"  [-] 导出失败: {result}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"  [-] 导出 Excel 失败: {e}")
            return None

    def _fix_download_url(self, url: str) -> str:
        """修复语雀返回的不完整 URL"""
        if url and url.startswith('/'):
            return 'https://www.yuque.com' + url
        return url

    def _download_file(self, url: str, filename: str, sub_dir: str = None) -> str:
        """下载文件"""
        # 清理文件名
        safe_filename = self._sanitize_filename(filename)

        # 确定目标目录
        if sub_dir:
            target_dir = self.output_dir / sub_dir
            target_dir.mkdir(parents=True, exist_ok=True)
        else:
            target_dir = self.output_dir

        filepath = target_dir / safe_filename

        try:
            response = self.session.get(url, stream=True)
            response.raise_for_status()

            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

            print(f"  [+] 已保存: {sub_dir}/{safe_filename}" if sub_dir else f"  [+] 已保存: {safe_filename}")
            return str(filepath)
        except requests.exceptions.RequestException as e:
            print(f"  [-] 下载失败: {e}")
            return None

    def _sanitize_filename(self, filename: str) -> str:
        """清理文件名，移除非法字符和emoji"""
        illegal_chars = '<>:"/\\|?*'
        for char in illegal_chars:
            filename = filename.replace(char, '_')
        # 移除 emoji 和其他非法 Unicode 字符
        filename = filename.encode('utf-8', errors='ignore').decode('utf-8')
        # 替换 Windows 不支持的字符
        filename = filename.replace('\u200b', '')  # 零宽空格
        filename = filename.replace('\ufeff', '')  # BOM
        return filename.strip()

    def export_all(self, export_markdown: bool = True, export_pdf: bool = False):
        """导出所有知识库的所有文档"""
        books = self.get_all_books()

        if not books:
            print("没有找到知识库或获取失败")
            return

        print(f"\n开始导出，共 {len(books)} 个知识库...")
        print("=" * 60)

        total_success = 0
        total_fail = 0

        for book_idx, book in enumerate(books, 1):
            book_id = book.get('id')
            book_name = book.get('name', f'book_{book_id}')
            stack_name = book.get('stack_name', '默认分组')
            items_count = book.get('items_count', 0)

            print(f"\n{'='*60}")
            print(f"[{book_idx}/{len(books)}] 知识库: {book_name} (共 {items_count} 个文档)")
            print(f"{'='*60}")

            # 获取该知识库下的文档列表
            docs = self.get_docs_list(str(book_id))

            if not docs:
                print(f"  [!] 该知识库没有文档或获取失败")
                continue

            print(f"  获取到 {len(docs)} 个文档")

            # 为该知识库创建文件夹: 输出目录/知识库名称/Doc文档 或 Sheet表格
            book_dir = self.output_dir / book_name

            doc_dir = book_dir / "Doc文档"
            sheet_dir = book_dir / "Sheet表格"
            doc_dir.mkdir(parents=True, exist_ok=True)
            sheet_dir.mkdir(parents=True, exist_ok=True)

            success_count = 0
            fail_count = 0

            for i, doc in enumerate(docs, 1):
                doc_id = doc.get('id')
                title = doc.get('title', f'doc_{doc_id}')
                doc_type = doc.get('type', 'Doc')

                print(f"\n  [{i}/{len(docs)}] {title} (类型: {doc_type})")

                try:
                    if doc_type == 'Doc':
                        if export_markdown:
                            result = self.export_doc_markdown(doc_id, title, f"{book_name}/Doc文档")
                            if result:
                                success_count += 1
                            else:
                                fail_count += 1

                        if export_pdf:
                            time.sleep(0.5)
                            result = self.export_doc_pdf(doc_id, title, f"{book_name}/Doc文档")
                            if result:
                                success_count += 1
                            elif not export_markdown:
                                fail_count += 1

                    elif doc_type == 'Sheet':
                        result = self.export_sheet_excel(doc_id, title, f"{book_name}/Sheet表格")
                        if result:
                            success_count += 1
                        else:
                            fail_count += 1
                    else:
                        print(f"  [-] 不支持的文档类型: {doc_type}")
                        fail_count += 1

                    time.sleep(0.3)

                except Exception as e:
                    print(f"  [-] 处理文档时出错: {e}")
                    fail_count += 1

            print(f"\n  {book_name} 导出完成: 成功 {success_count}, 失败 {fail_count}")
            total_success += success_count
            total_fail += fail_count

        print("\n" + "=" * 60)
        print(f"全部导出完成!")
        print(f"  成功: {total_success}, 失败: {total_fail}")
        print(f"文件保存在: {self.output_dir.absolute()}")


def main():
    """主函数"""
    # 配置参数
    OUTPUT_DIR = "exported_docs"  # 输出目录

    print("=" * 60)
    print("语雀文档导出工具")
    print("=" * 60)

    exporter = YuqueExporter(output_dir=OUTPUT_DIR)

    # 导出所有文档
    # export_markdown=True: 导出为 Markdown
    # export_pdf=True: 同时导出为 PDF (注意: 语雀 API 不支持查询 PDF 导出状态)
    exporter.export_all(export_markdown=True, export_pdf=False)


if __name__ == "__main__":
    main()

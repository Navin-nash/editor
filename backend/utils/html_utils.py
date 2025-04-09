from html2docx import html2docx
import pdfkit
import tempfile
from bs4 import BeautifulSoup


def html_to_docx(html: str, output_path: str):
    html2docx(html, output_path)


def html_to_pdf(html: str, output_path: str):
    styled_html = f"""
    <html>
    <head>
    <style>
    body {{ font-family: Arial, sans-serif; }}
    p {{ margin: 10px 0; }}
    img {{ max-width: 100%; height: auto; }}
    </style>
    </head>
    <body>{html}</body>
    </html>
    """
    pdfkit.from_string(styled_html, output_path)


def html_to_hwpx(html: str, output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("<!-- HWPX Export Placeholder -->\n")
        f.write(f"<body>{html}</body>")
from docx import Document
from bs4 import BeautifulSoup
import io
import base64
from PIL import Image

def parse_docx(file_bytes):
    document = Document(io.BytesIO(file_bytes))
    html = ""

    for para in document.paragraphs:
        style = f"text-align:{para.alignment.name.lower() if para.alignment else 'left'};"
        if para.style.font:
            font = para.style.font
            if font.name:
                style += f"font-family:{font.name};"
            if font.size:
                style += f"font-size:{font.size.pt}px;"
            if font.color and font.color.rgb:
                style += f"color:#{font.color.rgb};"

        html += f"<p style='{style}'>"
        for run in para.runs:
            tag = ""
            if run.bold:
                tag += "<strong>"
            if run.italic:
                tag += "<em>"
            html += f"{tag}{run.text}{'</em>' if run.italic else ''}{'</strong>' if run.bold else ''}"
        html += "</p>"

    return html

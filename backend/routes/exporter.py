from fastapi import APIRouter, Request
from fastapi.responses import FileResponse
from utils.html_utils import html_to_docx, html_to_pdf, html_to_hwpx
import uuid
import os

router = APIRouter()
EXPORT_PATH = "static/exports"
os.makedirs(EXPORT_PATH, exist_ok=True)

@router.post("/export/{format}")
async def export_html(format: str, req: Request):
    data = await req.json()
    html = data.get("html", "")
    file_id = str(uuid.uuid4())

    if format == "pdf":
        out_path = os.path.join(EXPORT_PATH, f"{file_id}.pdf")
        html_to_pdf(html, out_path)
    elif format == "docx":
        out_path = os.path.join(EXPORT_PATH, f"{file_id}.docx")
        html_to_docx(html, out_path)
    elif format == "hwpx":
        out_path = os.path.join(EXPORT_PATH, f"{file_id}.hwpx")
        html_to_hwpx(html, out_path)
    else:
        return {"error": "Invalid export format"}

    return FileResponse(out_path, media_type="application/octet-stream", filename=os.path.basename(out_path))

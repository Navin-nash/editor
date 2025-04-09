from fastapi import APIRouter, UploadFile, File
from utils.docx_utils import parse_docx
from utils.hwpx_utils import parse_hwpx
import os

router = APIRouter()

@router.post("/parse")
async def parse_document(file: UploadFile = File(...)):
    ext = os.path.splitext(file.filename)[-1].lower()
    if ext == ".docx":
        return {"html": parse_docx(await file.read())}
    elif ext == ".hwpx":
        return {"html": parse_hwpx(await file.read())}
    else:
        return {"error": "Unsupported file type"}
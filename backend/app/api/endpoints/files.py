from fastapi import APIRouter, UploadFile, File, HTTPException
from app.api.services.elt_process import process_files

router = APIRouter()

@router.post("/upload-files/")
async def upload_files(payment_report: UploadFile = File(...), mtr_report: UploadFile = File(...)):
    try:
        print(f"Received file: {payment_report.filename} of size {payment_report.size}")
        print(f"Received file: {mtr_report.filename} of size {mtr_report.size}")

        process_files(payment_report, mtr_report)

        return {"message": "Files processed and loaded successfully"}
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

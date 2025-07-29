from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile, Form
from sqlalchemy.orm import Session
from app.database import get_db
from app.domain import FileCreate, FileUpdate, FileResponse
from app.services import file_service, note_service
from app.auth import get_current_user
import boto3
import os

router = APIRouter(prefix="/files", tags=["files"])

s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_DEFAULT_REGION", "us-east-1")
)

BUCKET_NAME = os.getenv("BUCKET_NAME", "fast-notes-bucket")

@router.post("/upload", response_model=FileResponse, status_code=status.HTTP_201_CREATED)
async def upload_file(
    note_id: int = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    try:
        note = note_service.get_by_id(db, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        if note.user_id != current_user.id:
            raise HTTPException(status_code=401, detail="User not authorized to add files to this note")
        s3_key = f"notes/{note_id}/{file.filename}"
        s3_client.upload_fileobj(
            file.file, 
            BUCKET_NAME, 
            s3_key,
            ExtraArgs={'ContentType': file.content_type}
        )
        
        file_url = f"https://{BUCKET_NAME}.s3.{os.getenv('AWS_DEFAULT_REGION')}.amazonaws.com/{s3_key}"
        
        file_data = FileCreate(
            name=file.filename,
            url=file_url,
            type=file.content_type,
            note_id=note_id
        )
        
        return file_service.create(db, file_data)
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Upload failed: {str(e)}")
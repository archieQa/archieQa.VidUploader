from fastapi import FastAPI, UploadFile, HTTPException
from pathlib import Path
import os
from config.settings import UPLOAD_DIRECTORY, ALLOWED_EXTENSIONS, MAX_FILE_SIZE_MB

app = FastAPI()

def save_file(file: UploadFile, directory: str):
    # Ensure the directory exists
    Path(directory).mkdir(parents=True, exist_ok=True) # Create directory if it doesn't exist

    file_path = Path(directory) / file.filename # Save file to directory
    with open(file_path, "wb") as buffer: # Write file to disk in chunks
        buffer.write(file.file.read()) # Read file in chunks to prevent memory issues
    return file_path # Return file path for reference

def validate_file(file: UploadFile):
    # Check file extension
    if Path(file.filename).suffix.lower() not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Unsupported file type.")
    # Check file size
    file.file.seek(0, os.SEEK_END)
    file_size_mb = file.file.tell() / (1024 * 1024)
    if file_size_mb > MAX_FILE_SIZE_MB:
        raise HTTPException(status_code=400, detail="File size exceeds limit.")
    file.file.seek(0)  # Reset file pointer
    return True

@app.post("/upload/")
async def upload_video(file: UploadFile):
    validate_file(file)
    file_path = save_file(file, UPLOAD_DIRECTORY)
    return {"file_path": str(file_path)}

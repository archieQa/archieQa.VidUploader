import os
from dotenv import load_dotenv

load_dotenv()

UPLOAD_DIRECTORY = os.getenv("UPLOAD_DIRECTORY", "./uploads")
ALLOWED_EXTENSIONS = {".mp4", ".mov", ".avi"}
MAX_FILE_SIZE_MB = 200  # Example limit

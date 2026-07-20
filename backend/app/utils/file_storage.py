import os
import uuid
from pathlib import Path

UPLOAD_DIR = Path("app/uploads/tickets")

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def save_upload(file):

    extension = os.path.splitext(file.filename)[1]

    stored_name = f"{uuid.uuid4()}{extension}"

    destination = UPLOAD_DIR / stored_name

    with open(destination, "wb") as buffer:
        buffer.write(file.file.read())

    return stored_name, str(destination)
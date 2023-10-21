from fastapi import UploadFile
from .api.generated.resources.file_upload.service.service import AbstractFileUploadService


class FileUploadService(AbstractFileUploadService):
    def upload_file(self, *, file: UploadFile):
        contents = file.file.read()
        print(len(contents))

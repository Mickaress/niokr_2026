import uuid
import os

MAX_LENGTH_FIELD = 255
MAX_LENGTH_TEXT = 1500


def project_file_upload_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    return f'projects/{instance.project.id}/{uuid.uuid4().hex}{ext}'

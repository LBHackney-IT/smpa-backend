import os
import uuid
import boto3
import envkey  # NOQA
import mimetypes
from io import BytesIO

from smpa.helpers.console import console


class S3:

    _CHUNK_SIZE_BYTES = 4096
    _BUCKET_NAME = 'smpa-documents'

    def __init__(self):
        self.client = boto3.client(
            's3',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
            endpoint_url=os.environ.get('AWS_S3_ENDPOINT_URL')
        )
        self.bucket = self.client.create_bucket(Bucket=self._BUCKET_NAME)

    @property
    def bucket_name(self):
        return self._BUCKET_NAME

    def save(self, file_obj, path):

        while True:
            chunk = file_obj.file.read(self._CHUNK_SIZE_BYTES)
            if not chunk:
                break

            buffer = BytesIO()
            buffer.write(chunk)

        buffer.seek(0)
        try:
            self.client.upload_fileobj(
                buffer,
                'smpa-documents',
                path,
                ExtraArgs={
                    "ACL": 'private',
                    "ContentType": file_obj.type
                }
            )
        except Exception as e:
            buffer.close()
            console.error(e)
            return False

        buffer.close()

        return True


s3 = S3()

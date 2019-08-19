import os
import uuid
import boto3
import envkey  # NOQA
import mimetypes
from io import BytesIO

from smpa.helpers.console import console


class S3:

    _CHUNK_SIZE_BYTES = 4096

    def __init__(self):
        if os.environ.get('AWS_S3_ENDPOINT_URL', None) is not None:
            self.client = boto3.client(
                's3',
                aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
                endpoint_url=os.environ.get('AWS_S3_ENDPOINT_URL')
            )
        else:
            self.client = boto3.client(
                's3',
                aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
                region_name=os.environ.get('AWS_REGION_NAME')
            )

    @property
    def bucket_name(self):
        self._BUCKET_NAME = os.environ.get('AWS_BUCKET_NAME')
        if not hasattr(self, 'bucket'):
            try:
                self.bucket = self.client.create_bucket(
                    Bucket=self._BUCKET_NAME,
                    CreateBucketConfiguration={
                        'LocationConstraint': os.environ.get('AWS_REGION_NAME')
                    }
                )
            except Exception:
                pass
        return self._BUCKET_NAME

    def fetch(self, path):
        buffer = BytesIO()
        self.client.download_fileobj(self.bucket_name, path, buffer)
        buffer.seek(0)
        return buffer

    def save(self, file_obj, path):

        buffer = BytesIO()
        while True:
            chunk = file_obj.file.read(self._CHUNK_SIZE_BYTES)
            if not chunk:
                break

            buffer.write(chunk)

        buffer.seek(0)
        try:
            self.client.upload_fileobj(
                buffer,
                self.bucket_name,
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

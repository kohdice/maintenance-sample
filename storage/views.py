import os

import boto3
from django.http import HttpResponse
from django.views.generic import TemplateView

from config import settings


class IndexView(TemplateView):
    template_name = "storage/loader.html"


index = IndexView.as_view()


def upload_file(request):
    s3 = boto3.resource(
        service_name="s3",
        endpoint_url=os.environ["ENDPOINT"],
        aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
        region_name="",
    )

    bucket = s3.Bucket(os.environ["S3_BUCKET_NAME"])

    file_name = "test.png"
    file_path = f"{settings.BASE_DIR}/{file_name}"

    bucket.upload_file(file_path, file_name)
    return HttpResponse("Upload Complete")

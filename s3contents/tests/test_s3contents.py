import os

import pytest

from s3contents import S3ContentsManager

@pytest.mark.s3
def test_bucket_access():
    import logging

    try:
        logger = logging.getLogger()
        contents_manager = S3ContentsManager(
            access_key_id=os.environ.get("AWS_ACCESS_KEY_ID", None),
            secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY", None),
            session_token=os.environ.get("AWS_SESSION_TOKEN", None),
            bucket="exploration-dev-datap",
            region_name="eu-west-1"
        )
    except OSError as e:
        pytest.fail("Unexpected Error ..", e)

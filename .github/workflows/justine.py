import os
from b2sdk.v2 import InMemoryAccountInfo, B2Api

# --- Configuration ---
APPLICATION_KEY_ID = '005e0e146db57d50000000001'
APPLICATION_KEY    = 'K005LdurEh/NDp4F7k8oAo/hBO2+dqE'
BUCKET_NAME        = 'justine2'
LOCAL_FOLDER       = 'downloads/'
B2_PREFIX          = ''  # Optional

# --- Authenticate ---
info = InMemoryAccountInfo()
b2_api = B2Api(info)
b2_api.authorize_account("production", APPLICATION_KEY_ID, APPLICATION_KEY)
bucket = b2_api.get_bucket_by_name(BUCKET_NAME)

# --- Upload Function ---
def upload_directory_recursively(local_folder, bucket, b2_prefix=''):
    for root, _, files in os.walk(local_folder):
        for file in files:
            local_path = os.path.join(root, file)
            rel_path = os.path.relpath(local_path, local_folder).replace("\\", "/")
            b2_path = os.path.join(b2_prefix, rel_path).replace("\\", "/")

            print(f"Uploading {local_path} → b2://{bucket.name}/{b2_path}")
            with open(local_path, 'rb') as f:
                bucket.upload_bytes(f.read(), b2_path)

upload_directory_recursively(LOCAL_FOLDER, bucket, B2_PREFIX)

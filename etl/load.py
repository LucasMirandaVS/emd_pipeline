from google.cloud import storage
import os

def upload_to_gcs(local_path: str, bucket_name: str, gcs_prefix="terceirizados"):
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    blob_path = os.path.join(gcs_prefix, os.path.relpath(local_path, "data"))
    blob = bucket.blob(blob_path)
    blob.upload_from_filename(local_path)
    print(f"✔️ Enviado para GCS: {blob_path}")

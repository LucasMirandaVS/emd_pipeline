from prefect import flow, task
from etl.extract import get_csv_links
from etl.transform import process_csv_from_url
from etl.load import upload_to_gcs
import os
from dotenv import load_dotenv

load_dotenv()

@task
def process_and_upload(link: str, bucket_name: str):
    local_path = process_csv_from_url(link)
    upload_to_gcs(local_path, bucket_name)

@flow(name="Terceirizados_ETL_Flow")
def main_flow():
    bucket_name = os.getenv("GCS_BUCKET")
    links = get_csv_links()
    for link in links:
        process_and_upload.submit(link, bucket_name)

if __name__ == "__main__":
    main_flow()

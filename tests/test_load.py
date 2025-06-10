from etl.load import upload_to_gcs
from unittest import mock

@mock.patch("etl.load.storage.Client")
def test_upload_to_gcs(mock_storage_client):
    # Mocks
    mock_bucket = mock.Mock()
    mock_blob = mock.Mock()
    mock_bucket.blob.return_value = mock_blob
    mock_storage_client.return_value.bucket.return_value = mock_bucket

    # Executa função
    upload_to_gcs("data/ano=2022/mes=01/terceirizados-2022-01.csv", "fake-bucket")

    # Verifica se blob.upload_from_filename foi chamado
    mock_blob.upload_from_filename.assert_called_once()

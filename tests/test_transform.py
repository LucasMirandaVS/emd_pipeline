from etl.transform import process_csv_from_url
import os

def test_process_csv_from_url():
    test_url = "https://arquivos-dados-abertos.s3.amazonaws.com/terceirizados/terceirizados-2022-01.csv"
    output_path = process_csv_from_url(test_url, local_base="data_test/")
    
    assert os.path.exists(output_path)
    assert output_path.endswith(".csv")

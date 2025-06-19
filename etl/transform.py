# etl/transform.py
import polars as pl
import os
from io import BytesIO
import requests

def process_csv_from_url(url: str, local_base="data/") -> str:
    filename = url.split("/")[-1]
    ano, mes = filename.split("-")[1:3]
    mes = mes.replace(".csv", "")

    response = requests.get(url)
    df = pl.read_csv(BytesIO(response.content))

    df = df.with_columns([
        pl.lit(ano).alias("ano"),
        pl.lit(mes).alias("mes")
    ])

    output_dir = os.path.join(local_base, f"ano={ano}", f"mes={mes}")
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, filename)
    df.write_csv(output_path)

    return output_path

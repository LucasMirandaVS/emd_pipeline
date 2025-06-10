# tests/test_get_excel.py

import polars as pl
import pandas as pd
import requests
from io import BytesIO

def test_download_and_parse_excel():
    url = "https://www.gov.br/cgu/pt-br/acesso-a-informacao/dados-abertos/arquivos/terceirizados/arquivos/terceirizados202501.xlsx"

    # Faz o download do arquivo
    response = requests.get(url)
    assert response.status_code == 200, "Falha ao baixar o arquivo Excel"

    # Lê com pandas e converte tudo para string
    df_pd = pd.read_excel(BytesIO(response.content)).astype(str)

    # Converte para polars
    df = pl.from_pandas(df_pd)

    # Verifica se há dados
    assert df.shape[0] > 0, "DataFrame está vazio"

    # Verifica se colunas esperadas estão presentes
    expected_cols = {"id_terc", "nm_ug_tabela_ug", "vl_mensal_salario", "Mes_Carga", "Ano_Carga"}
    assert expected_cols.issubset(set(df.columns)), "Colunas esperadas não encontradas no DataFrame"

Projeto de engenharia de dados desenvolvido como solução para um desafio técnico. O objetivo é construir um pipeline de dados que realiza a extração, transformação e carga (ETL) de dados públicos disponibilizados pela CGU (Controladoria-Geral da União) sobre trabalhadores terceirizados.

---

## Tecnologias e Ferramentas

- Python 3.10+
- `polars` para processamento de dados
- Google Cloud Storage (GCS) para armazenamento
- Prefect 2.0 para orquestração (com Docker)
- Pytest para testes automatizados

---

## Descrição do Pipeline

1. **Extração (Extract)**
   - Download de planilhas públicas `.xlsx` contendo dados de terceirizados da CGU.

2. **Transformação (Transform)**
   - Conversão e limpeza dos dados.
   - Criação da coluna `data_referencia` a partir de `Ano_Carga` e `Mes_Carga`.
   - Normalização dos tipos de dados.

3. **Carga (Load)**
   - Escrita dos dados em formato CSV no Google Cloud Storage, utilizando particionamento por ano e mês.

4. **Orquestração**
   - Toda a pipeline é executada via Prefect 2.0, empacotada em um container Docker.




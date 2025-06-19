import requests
from bs4 import BeautifulSoup

def get_csv_links():
    url = "https://www.gov.br/cgu/pt-br/acesso-a-informacao/dados-abertos/arquivos/terceirizados"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    links = [
        a["href"]
        for a in soup.find_all("a", href=True)
        if a["href"].endswith(".csv") and "terceirizados" in a["href"]
    ]
    
    return links

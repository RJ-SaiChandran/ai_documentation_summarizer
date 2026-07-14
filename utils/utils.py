import requests
from bs4 import BeautifulSoup

def fetch_doc_contents(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

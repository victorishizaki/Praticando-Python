import requests # responsável pela requisição
from bs4 import BeautifulSoup # responsável pela extração de dados

url = "https://g1.globo.com" # URL do site que você deseja coletar dados

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    # '(KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36
}

resposta = requests.get(url)  # Faz a requisição GET para a URL

if resposta.status_code == 200: # Verifica se a requisição foi bem sucedida
    # código 200 -> sucesso
    print("Requisição feita com sucesso")
    # print(resposta.text) # retorno
    # preenchendo nossa sopa
    soup = BeautifulSoup(resposta.text, "html.parser")
    # encontrando as notícias
    noticias = soup.find_all("a", class_="feed-post-link")
    
    print("Últimas noticias dp G1:")
    for index , noticia in enumerate(noticias):
        print(f"Noticia {index+1}. {noticia.text.strip()} - {noticia['href']} ")
    

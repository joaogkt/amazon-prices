from bs4 import BeautifulSoup
import requests
import pandas as pd

pesquisa = 'Computador'
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
URL = f"https://www.amazon.com.br/s?k={pesquisa}"
HEADERS = ({'User-Agent': user_agent, 'Accept-Language': 'pt-BR'})
webpage = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(webpage.content, "html.parser")


nomes = soup.find_all("span", attrs={"class": "a-size-base-plus a-color-base a-text-normal"})
precos = soup.find_all("span", attrs={"class": "a-price-whole"})
avaliacoes = soup.find_all("span", attrs={"class": "a-icon-alt"})
links = soup.find_all("a", attrs={"class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})
min_length = min(len(nomes), len(precos), len(avaliacoes), len(links))

dados = {}

for i in range(min_length):
    nome = nomes[i].text
    preco = precos[i].text
    avaliacao = avaliacoes[i].text
    link = links[i]['href']

    dados[nome] = {
        'Preço': preco,
        'Avaliacao': avaliacao,
        'Link': "https://amazon.com.br" + link
    }

amazon_df = pd.DataFrame.from_dict(dados)
amazon_df.to_csv("amazon_data.csv", header=True, index=False)


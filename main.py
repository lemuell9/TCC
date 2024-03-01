#Obtem todos os links (href attributes) fe sebrae.com.br
import requests
import string

from collections import Counter

from bs4 import BeautifulSoup

url = "https://www.climatempo.com.br/"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
links = soup.findAll("a")

news_urls = []
for link in links:
  ##print(link)
  href = link.get("href")
  if href and href.startswith("/"):
    news_url = "https://www.climatempo.com.br/" + href
    news_urls.append(news_url)
  elif href and href.find('ufpa.br/'):
    news_urls.append(href)

##quit()
##Busca por todos os nome próprios (nomes de pessoas)
##nos 10 primeiros links retornados
all_nouns = []
for url in news_urls[:10]:
  if url.startswith("http"):
    print("Fetching {}".format(url))
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    words = soup.text.split()
    nouns = [
        word for word in words
        if word.isalpha() and word[0] in string.ascii_uppercase
    ]
    all_nouns += nouns

print(Counter(all_nouns).most_common(100))

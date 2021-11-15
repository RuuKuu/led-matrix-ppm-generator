import requests
from bs4 import BeautifulSoup
from ppm import create_ppm, merge_ppm

url = requests.get("https://www.sendai-nct.ac.jp/")
soup = BeautifulSoup(url.text, "html.parser")

news_titles = soup.select("#tab1 .n_text")

for i, news_title in enumerate(news_titles):
  if i == 0:
    titles = news_title.get_text()
  else:
    titles += "   " + news_title.get_text()

create_ppm("0", titles, 255,0,0,255,255,255)
merge_ppm()
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
  
  titles = "           " +titles + "           "

create_ppm("1_0_KosenNews", titles, 20, 255, 255, 255, 0, 0, 0)
#merge_ppm()
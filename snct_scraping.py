import requests
from bs4 import BeautifulSoup
from create_ppm import CreatePPM
import time

url = requests.get("https://www.sendai-nct.ac.jp/")
soup = BeautifulSoup(url.text, "html.parser")

news_titles = soup.select("#tab1 .n_text")

for i, news_title in enumerate(news_titles):
  if i == 0:
    titles = news_title.get_text()
  else:
    titles += "   " + news_title.get_text()
  
titles = "   " +  " 【仙台高専 新着情報  " + str(time.strftime('%H:%M')) + " 取得】  " +titles + "           "

ob = CreatePPM()
ob.create_ppm(show_line=2, show_no=1, show_sec=1, name="KosenNEWS", text=titles, text_r=255, text_g=140, text_b=0, bg_r=0, bg_g=0, bg_b=0)

#鉄道オレンジ　255,136,000
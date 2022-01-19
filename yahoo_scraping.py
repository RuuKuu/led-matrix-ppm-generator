import feedparser
from ppm import create_ppm, merge_ppm
from create_ppm import CreatePPM
import time

#d = feedparser.parse(r"https://news.yahoo.co.jp/rss/topics/top-picks.xml")
d = feedparser.parse(r"https://news.yahoo.co.jp/rss/categories/domestic.xml")

for i, entry in enumerate(d.entries):
  if i == 0:
    titles = entry.title
  elif i == 7:
    break
  else:
    titles += "   " + entry.title

titles = "        "+  " 【取得元・出典:Yahoo!ニュース RSS [国内]  " + str(time.strftime('%H:%M')) + " 取得】  "  + titles + "           "

ob = CreatePPM()
ob.create_ppm(show_line=2, show_no=2, show_sec=1, name="YahooNEWS_Main", text=titles, text_r=255, text_g=255, text_b=0, bg_r=0, bg_g=0, bg_b=0)


d = feedparser.parse(r"https://news.yahoo.co.jp/rss/media/tbcv/all.xml")

for i, entry in enumerate(d.entries):
  if i == 0:
    titles = entry.title
  elif i == 6:
    break
  else:
    titles += "   " + entry.title

titles = "        "+  " 【取得元・出典:Yahoo!ニュース RSS [tbc東北放送]  " + str(time.strftime('%H:%M')) + " 取得】  "  + titles + "           "

ob.create_ppm(show_line=2, show_no=3, show_sec=1, name="YahooNEWS_tbc", text=titles, text_r=0, text_g=255, text_b=255, bg_r=0, bg_g=0, bg_b=0)
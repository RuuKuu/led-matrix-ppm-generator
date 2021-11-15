import feedparser
from ppm import create_ppm, merge_ppm

d = feedparser.parse(r"https://news.yahoo.co.jp/rss/topics/top-picks.xml")

for i, entry in enumerate(d.entries):
  if i == 0:
    titles = entry.title
  else:
    titles += "   " + entry.title

create_ppm("1", titles, 255,255,0,255,255,255)
merge_ppm()
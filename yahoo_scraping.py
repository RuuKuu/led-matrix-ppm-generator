import feedparser
from ppm import create_ppm, merge_ppm

d = feedparser.parse(r"https://news.yahoo.co.jp/rss/topics/top-picks.xml")

for i, entry in enumerate(d.entries):
  if i == 0:
    titles = entry.title
  else:
    titles += "   " + entry.title

titles = "        " + titles + "           "

create_ppm("Line2/2_0_YahooNews", titles, 20, 255, 0, 255, 0, 0, 0)
#merge_ppm()
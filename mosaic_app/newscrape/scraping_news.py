# coding: UTF-8
import feedparser
import urllib


def scrape_news(keyword, entry_num):

    # URLエンコーディング
    k = urllib.parse.quote(keyword)
    url = "https://news.google.com/news/rss/search/section/q/" + k + "/" + k + "?ned=jp&hl=ja&gl=JP"

    d = feedparser.parse(url)
    news = list()

    for i, entry in enumerate(d.entries[:entry_num], 1):
        p = entry.published_parsed
        sortkey = "%04d%02d%02d%02d%02d%02d" % (p.tm_year, p.tm_mon, p.tm_mday, p.tm_hour, p.tm_min, p.tm_sec)

        tmp = {
            "no": i,
            "title": entry.title,
            "link": entry.link,
            "published": entry.published,
            "sortkey": sortkey
        }

        news.append(tmp)

    news = sorted(news, key=lambda x: x['sortkey'], reverse=True)

    return news


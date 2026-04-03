import feedparser
import certifi
import requests
from jsonResolve import load_json


def parse_feeds_to_list():


    rss_url_list=[]#ill put them in list to make it scalable for multiple feeds from future json
    rss_url_list.append("https://feeds.bbci.co.uk/news/rss.xml")
    rss_url_list=load_json("feeds_list.json",rss_url_list)
    final_parse_list = []




    for url in rss_url_list:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0"
            }

            response = requests.get(
                url,
                headers=headers,
                verify=certifi.where(),
                timeout=10
            )
            feed = feedparser.parse(response.content)
        except Exception as e:
            print("RSS fetch failed:", e)
            return []
        print("RSS fetch success:", feed.feed.title)
        for entry in feed.entries:
            string = ""  # start temp internal string
            string += getattr(feed.feed,"title","") + ": "  # start it with news source name
            string += getattr(entry, "title","") + "," #add to its the news name
            string += getattr(entry, "summary","") + "," # add the description
            final_parse_list.append([string,getattr(entry, "link","")]) # make list of dictionaries {string,link}
            #rinse and repeat
    # print(final_parse_list)

    return final_parse_list # this is a list of two item lists ,each has first item string,other link of the string








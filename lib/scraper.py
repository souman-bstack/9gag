import json
import ssl
import urllib.request
from lib.gag import Gag
from bs4 import BeautifulSoup

def scrap_gags():
    ssl._create_default_https_context = ssl._create_unverified_context
    gags_url = "https://9gag.com/v1/group-posts/group/default/type/hot"
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"

    req = urllib.request.Request(gags_url, data=None, headers={'User-Agent': user_agent})

    response = urllib.request.urlopen(req).read().decode('utf-8')

    gags = json.loads(response)['data']['posts']
    Gag.save_gags(gags)

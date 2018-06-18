import urllib.request as urllib2
import json

# check http://open.weibo.com/wiki/Short_url/share/statuses
TOKEN = "3108863132"
ROOT_URL = "http://api.t.sina.com.cn"
SHORTEN = "/short_url/shorten.json?source={}&url_long={}"

class SinaSURLHelper:
    def shorten_url(self, longurl):
        try:
            url = ROOT_URL + SHORTEN.format(TOKEN, longurl)
            response = urllib2.urlopen(url).read()
            jr = json.loads(response)
            return jr[0]['url_short']
        except Exception as e:
            print(e)

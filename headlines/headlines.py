from flask import Flask
from flask import render_template
from flask import request

import feedparser

app = Flask(__name__, template_folder='templates')

RSS_FEEDS = {'bbc':"http://feeds.bbci.co.uk/news/rss.xml",
             'cnn':"http://rss.cnn.com/rss/edition.rss",
             'fox':"http://feeds.foxnews.com/foxnews/latest",
             'iol':"http://www.iol.co.za/cmlink/1.640",
             'netease':"http://news.163.com/special/00011K6L/rss_newstop.xml"}

@app.route("/")
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEEDS:
        publication = "bbc"
    else:
        publication = query.lower()

    feed = feedparser.parse(RSS_FEEDS[publication])
    articles = feed['entries']
    return render_template("home.html",articles=articles)

if __name__ == '__main__':
    app.run(port=5000, debug=True)


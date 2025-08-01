import os
from flask import Flask, jsonify
import feedparser

app = Flask(__name__)

RSS_FEED_URL = "https://cointelegraph.com/rss/tag/cardano"

@app.route("/news")
def get_news():
    feed = feedparser.parse(RSS_FEED_URL)
    articles = []
    for entry in feed.entries[:5]:
        articles.append({
            "title": entry.title,
            "link": entry.link
        })
    return jsonify(articles)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)), debug=True)

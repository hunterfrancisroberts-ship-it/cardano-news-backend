from flask import Flask, jsonify
import feedparser

app = Flask(__name__)

@app.route("/news")
def get_news():
    url = "https://cointelegraph.com/rss/tag/cardano"
    feed = feedparser.parse(url)

    articles = []
    for entry in feed.entries[:5]:
        articles.append({
            "title": entry.title,
            "link": entry.link
        })

    return jsonify(articles)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)


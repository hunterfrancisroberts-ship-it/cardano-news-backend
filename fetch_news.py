import feedparser
from datetime import datetime

url = "https://cointelegraph.com/rss/tag/cardano"
feed = feedparser.parse(url)

html_output = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Cardano News Headlines</title>
  <style>
    body {
      font-family: sans-serif;
      background-color: #f6f8fa;
      padding: 20px;
      max-width: 700px;
      margin: auto;
    }
    h1 {
      text-align: center;
      color: #3c3c3c;
    }
    .card {
      background: white;
      margin: 15px 0;
      padding: 15px;
      border-radius: 10px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    a {
      color: #0077cc;
      text-decoration: none;
    }
  </style>
</head>
<body>
  <h1>📰 Latest Cardano News</h1>
"""

# Add real news
for entry in feed.entries[:5]:
    title = entry.title
    link = entry.link
    html_output += f"""
  <div class="card">
    <p><strong>{title}</strong></p>
    <a href="{link}">Read more</a>
  </div>
"""

html_output += """
</body>
</html>
"""

# Save to file
with open("news.html", "w") as f:
    f.write(html_output)

print("✅ News saved to 'news.html'. Run 'open news.html' to view.")

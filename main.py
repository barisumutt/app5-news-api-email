import requests
from send_email import send_email

topic = "tesla"
api_key = "3b74e7aabab643758956a199c7347554"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-04-14&sortBy=publishedAt&" \
      f"apiKey={api_key}" \
      "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ""
# Access the article titles and description
for article in content['articles'][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" \
               + "\n" + body + article['title'] + "\n" + \
               str(article['description']) \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
print("Your email was sent successfully!")
import requests
from send_email import send_email


api_key = "3b74e7aabab643758956a199c7347554"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-04-14&sortBy=publishedAt&apiKey=" \
      "3b74e7aabab643758956a199c7347554"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ""
# Access the article titles and description
for article in content['articles']:
    if article["title"] is not None:
        body = body + article['title'] + "\n" + str(article['description']) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
print("Your email was sent successfully!")
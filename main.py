import requests

api_key = "3b74e7aabab643758956a199c7347554"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-04-13&sortBy=publishedAt&apiKey=" \
      "3b74e7aabab643758956a199c7347554"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
      print(article["title"])
      print(article["description"])
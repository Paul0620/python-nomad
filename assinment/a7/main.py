import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"

# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
  return f"{base_url}/items/{id}"

db = {}
app = Flask("DayNine")

@app.route("/")
def home():
  order_by = request.args.get("order_by", "popular")
  if order_by not in db:
    print("Requesting")
    if order_by == 'popular':
      news = requests.get(popular)
    elif order_by == 'new':
      news = requests.get(new)
    results = list(news.json().values())[0]
    db[order_by] = results
  results = db[order_by]
  return render_template(
    "index.html",
    order_by = order_by,
    results=results
  )

@app.route("/<id>")
def detail(id): #id값을 받아줘야함
  comment = requests.get(make_detail_url(id)).json()
  return render_template(
    "detail.html",
    comment=comment
  )

app.run(host="0.0.0.0")
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
  order_by = request.args.get('order_by')
  if order_by:
    order_by = order_by.lower()

  if order_by == "new":
    link = new
  else:
    link = popular

  result = requests.get(link)
  print(request.args)
  json = result.json();
  news = json["hits"]

  
  return render_template("index.html" , news= news, order_by = order_by)

@app.route("/<id>")
def detail(id):
  result = requests.get(make_detail_url(id))
  detail = result.json();
  comments = detail['children']
  
  
  return render_template("detail.html" , detail=detail , comments = comments)
  


app.run(host="0.0.0.0")
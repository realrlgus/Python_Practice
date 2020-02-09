import google
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://trends.google.co.kr/trends/explore?date=now%201-d&geo=KR"

request = requests.get(f"{BASE_URL}&q=치킨")
result = BeautifulSoup(request.text, "html.parser")
table = result.find(
    "div", {"aria-label": "A tabular representation of the data in the chart."})
tr = table.find_all("tr")
for tds in tr:
    for td in tds.find_all("td"):
        print(td)

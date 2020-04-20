import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"


def get_brand(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    container = soup.find_all("ul", {"class": "goodsBox"})[1]
    items = container.find_all("a", {"class": "goodsBox-info"})

    for item in items:
        shop_title = item.find(
            "span", {"class": "company"}).get_text(strip=True)
        sub_link = item["href"]
        get_job(sub_link, shop_title)


def get_job(url, shop_title):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    container = soup.find("div", {"id": "NormalInfo"})
    jobs = container.find("table").find_all("tr", {"class": ""})[1:]
    job_count = container.find("p", {"class": "jobCount"}).find(
        "strong").get_text(strip=True)

    if job_count == "0":
        return
    csv_jobs = []
    print(f"crawling {shop_title} jobs...")
    for job in jobs:
        place = job.find("td", {"class": "local"}).get_text(strip=True)
        title = job.find("span", {"class": "title"}).get_text(strip=True)
        time = job.find("span", {"class": "time"}).get_text(strip=True)
        pay = job.find("span", {"class": "time"}).get_text(strip=True)
        date = job.find("td", {"class": "regDate"}).get_text(strip=True)

        csv_jobs.append({"place": place, "title": title,
                         "time": time, "pay": pay, "date": date})

    save_to_file(csv_jobs, shop_title)
    print(f"crawling {shop_title} complete!")


def save_to_file(jobs, shop_title):
    file = open(f"{shop_title}.csv", mode="w", encoding="UTF8")
    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "date"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return


get_brand(alba_url)

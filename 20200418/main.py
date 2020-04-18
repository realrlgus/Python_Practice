import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")


url = "https://www.iban.com/currency-codes"

request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")


countries = []
choice_countries = []


table = soup.find("table")
rows = table.find_all("tr")[1:]

for row in rows:
    items = row.find_all("td")
    name = items[0].text
    code = items[2].text
    if name and code:
        if name != "No universal currency":
            country = {
                'name': name.capitalize(),
                'code': code
            }
            countries.append(country)


def ask():
    try:
        choice = int(input("#: "))
        if choice > len(countries):
            print("Choose a number from the list.")
            ask()
        else:
            choice_countries.append(countries[choice])
            if len(choice_countries) == 1:
                print(choice_countries[0]['name'])
                print("\r\nNow Choose another country.")
                ask()
                print(choice_countries[1]['name'])

    except ValueError:
        print("That wasn't a number.")
        ask()


def money():
    try:
        return int(input("#: "))

    except ValueError:
        print("That wasn't a number.")
        money()


def get_currency(before, after, amount):
    url = f"https://transferwise.com/gb/currency-converter/{before}-to-{after}-rate?amount={amount}"
    print(url)
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")

    convert_money = soup.find("input", {"id": "cc-amount-to"})["value"]

    print(format_currency(amount, before, locale="ko_KR"), "is ",
          format_currency(convert_money, after, locale="ko_KR"))


for index, country in enumerate(countries):
    print(f"#{index} {country['name']}")

print("Choose a first country")
ask()

print(
    f"How many {choice_countries[0]['code']} do you want to convert to '{choice_countries[1]['code']}'? ")

price = money()

get_currency(choice_countries[0]['code'], choice_countries[1]['code'], price)



"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.macrotrends.net/stocks/charts/AAPL/apple/stock-price-history")
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find("table", {"class": "historical_data_table table"})
tbody = table.findChild('tbody')

data = []
strippedData = []
processed = []

for tr in tbody:
    for td in tr:
        for text in td:
            data.append(text.strip())

for d in data:
    if d != '':
        strippedData.append(d)

while len(strippedData) > 0:
    a = []
    for i in range(7):
        a.append(strippedData.pop())
    processed.append(a)
res = []
for d in processed:
    r = {
        'date': d[-1],
        'close_price': d[1]
    }
    res.append(r)

for k in res:
    print(k)

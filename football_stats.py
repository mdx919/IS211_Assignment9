import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/")
soup = BeautifulSoup(page.content, features="lxml")

table = soup.findAll("table", {"class": "TableBase-table"})
long_name = soup.findAll("span", {"class": "CellPlayerName--long"})
top_20_player_stats = []
for i in range(20):
    a = long_name[i].find('a')
    b = long_name[i].find("span", {"class": "CellPlayerName-position"})
    c = long_name[i].find("span", {"class": "CellPlayerName-team"})
    tr = soup.findAll("tr", {"class": "TableBase-bodyTr"})
    td = tr[i].findAll("td", {"class": "TableBase-bodyTd"})
    name = a.getText().strip()
    position = b.getText().strip()
    team = c.getText().strip()
    touchdowns = td[8].getText().strip()
    player = {
        'name': name,
        'position': position,
        'team': team,
        'touchdowns': touchdowns
    }
    top_20_player_stats.append(player)

for player in top_20_player_stats:
    print(player)


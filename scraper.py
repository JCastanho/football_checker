import requests
import json
from bs4 import BeautifulSoup

url = "https://desporto.sapo.pt/futebol/competicao/primeira-liga-2/classificacao"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
teste = soup.find_all("table", class_="rankings-table")[0].find_all('tr')

teams = []
for e in teste[1:]:
    s = e.text.split()
    if s[1] == "Portimonense":
        x = {
            "pos": s[0],
            "name":s[1],
            "points":s[2],
            "games":s[3],
            "wins":s[4],
            "draws":s[5],
            "loses":s[6],
            "GS":s[7],
            "GA":s[8],
            "GD":s[9] 
        }
        teams.append(x)
    if s[1] == "Gil":
        x = {
            "pos": s[0],
            "name":s[1]+" "+s[2]+" " + s[3],
            "points":s[4],
            "games":s[5],
            "wins":s[6],
            "draws":s[7],
            "loses":s[8],
            "GS":s[9],
            "GA":s[10],
            "GD":s[11] 
        }
        teams.append(x)
    else:
        x = {
            "pos": s[0],
            "name":s[1]+" "+s[2],
            "points":s[3],
            "games":s[4],
            "wins":s[5],
            "draws":s[6],
            "loses":s[7],
            "GS":s[8],
            "GA":s[9],
            "GD":s[10] 
        }
        teams.append(x)

with open("tables.json", "w") as outfile:
    json.dump(teams, outfile)
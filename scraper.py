import requests
import json
from bs4 import BeautifulSoup

url_base = "https://desporto.sapo.pt"
url = url_base + "/futebol/competicao/primeira-liga-2/classificacao"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
rankings_html = soup.find_all("table", class_="rankings-table")[0].find_all('tr')

teams_hrefs = soup.find_all("table", class_="rankings-table")[0].find_all("a", class_="[ ellipsis ]")
teams_urls = []
for i in teams_hrefs:
    link_url = i["href"]
    teams_urls.append(url_base + link_url)

new_page = requests.get(teams_urls[2])
new_soup = BeautifulSoup(new_page.content, "html.parser")
teste = new_soup.find_all("div", class_="[ column-group gutters ] communist")[0].text.split()

defesas_index = teste.index("Defesas")
medios_index = teste.index("Médios")
avanc_index = teste.index("Avançados")
nacionalidades = ["Portugal", "Brasil", "Ucrânia", "Suíça", "Grécia", "Bélgica", "Argentina", "Espanha", "Marrocos", "França", "Áustria", "Alemanha", "Uruguai", "Moçambique", "Ilhas de Cabo Verde", "República Democrática do Congo", "Guiné-Bissau", "Colômbia", "Sérvia", "México", "Irão", "Inglaterra", "Senegal", "Venezuela", "Japão", "Equador", "República Checa", "Hungria", "Mali", "Croácia", "Gana", "Costa do Marfim", "Camarões", "Israel", "Palestina", "Suécia", "Argélia", "Azerbaijão", "Eslovênia", "Canadá", "Chile"]
gr = []
defesas = []
medios = []
avanc = []

cont = 1

name = nac = position = ""

while cont < len(teste):
    if cont < defesas_index:
        if (teste[cont] != "Guarda-Redes" and teste[cont] not in nacionalidades):
            name += teste[cont] + " "    
        if (teste[cont] in nacionalidades):
            nac = teste[cont]
        if teste[cont] == "Guarda-Redes":
            position = teste[cont]
        if (name != "" and nac != "" and position != ""):
            x = {
                "name" : name,
                "nacionality" : nac,
                "position" : position
            }
            name = nac = position = ""
            gr.append(x)
    if defesas_index < cont < medios_index:
        if (teste[cont] != "Defesa" and teste[cont] not in nacionalidades and teste[cont] != "Defesas"):
            name += teste[cont] + " "    
        if (teste[cont] in nacionalidades):
            nac = teste[cont]
        if teste[cont] == "Defesa":
            position = teste[cont]
        if (name != "" and nac != "" and position != ""):
            y = {
                "name" : name,
                "nacionality" : nac,
                "position" : position
            }
            defesas.append(y)
            name = nac = position = ""
    if medios_index < cont < avanc_index:
        if (teste[cont] != "Médio" and teste[cont] not in nacionalidades and teste[cont] != "Médios"):
            name += teste[cont] + " "    
        if (teste[cont] in nacionalidades):
            nac = teste[cont]
        if teste[cont] == "Médio":
            position = teste[cont]
        if (name != "" and nac != "" and position != ""):
            z = {
                "name" : name,
                "nacionality" : nac,
                "position" : position
            }
            name = nac = position = ""
            medios.append(z)
    if avanc_index < cont:
        if (teste[cont] != "Avançado" and teste[cont] not in nacionalidades and teste[cont] != "Avançados"):
            name += teste[cont] + " "    
        if (teste[cont] in nacionalidades):
            nac = teste[cont]
        if teste[cont] == "Avançado":
            position = teste[cont]
        if (name != "" and nac != "" and position != ""):
            w = {
                "name" : name,
                "nacionality" : nac,
                "position" : position
            }
            avanc.append(w)
            name = nac = position = ""
    cont += 1

team = {
    "gr" : gr,
    "def" : defesas,
    "mid" : medios,
    "forw": avanc
}

with open("team.json", "w") as outfile:
    json.dump(team, outfile)

rankings = []
for e in rankings_html[1:]:
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
        rankings.append(x)
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
        rankings.append(x)
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
        rankings.append(x)

with open("tables.json", "w") as outfile:
    json.dump(rankings, outfile)
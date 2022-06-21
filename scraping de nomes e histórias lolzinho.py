import time

import requests
from bs4 import  BeautifulSoup
req = requests.get('https://www.leagueoflegends.com/pt-br/champions/')
if req.status_code == 200:
            print('Requisição bem sucedida!')
            content = req.content
            soup = BeautifulSoup(content, 'html.parser')
            table = soup.findAll( class_='style__Text-n3ovyt-3 gMLOLF')
            print('Os ultimos mangás que sairam hoje  no site https://www.supermangas.site/ são :\n')
            co = []

            for b in table:
                print('<li>', b.text, '</li>')
                co.append(b.text)
            for k in co:
                k=str(k).strip().lower().replace("'","")
                link='https://universe.leagueoflegends.com/pt_BR/story/champion/{}/'.format(k)
                req2=requests.get(link)
                print(co)
                print(link)

                content2 = req2.content
                soup2 = BeautifulSoup(content2, 'html.parser')
                table2 = soup2.findAll(property='og:description')

                print('Os ultimos mangás que sairam hoje  no site https://www.supermangas.site/ são :\n')
                for c in table2:
                    print('<li>', c, '</li>')




else:
            print('erro')

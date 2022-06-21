
import requests
from bs4 import  BeautifulSoup
req = requests.get('https://ge.globo.com/esports/lol/noticia/2022/02/18/campeoes-do-lol-lista-completa-de-personagens-e-funcoes.ghtml')
if req.status_code == 200:
            print('Requisição bem sucedida!')
            content = req.content
            soup = BeautifulSoup(content, 'html.parser')
            table = soup.findAll(class_='show-table__content show-table__content--highlight-top')
            print('Os ultimos mangás que sairam hoje  no site https://www.supermangas.site/ são :\n')
            co = []

            for b in table:
                d=str(b)
                d=d.replace('<td>','<div>')
                d=d.replace('</td>','</div> \n')
                print('<div>', d, '</div>')
                co.append(b.text)
            print(table)




else:
            print('erro')

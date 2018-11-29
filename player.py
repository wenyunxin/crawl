from bs4 import BeautifulSoup
import requests
import pymongo
import pandas as pd

client = pymongo.MongoClient('localhost', 27017)
myapp = client['myapp']
play = myapp['player']

url = 'https://basketball.realgm.com/nba/players#'

soup = BeautifulSoup(requests.get(url).text, 'lxml')
rows = soup.select('tbody > tr')
for row in rows:
    cols = row.findAll('td')
    data = {
        'number': cols[0].get_text(),
        'player': cols[1].get_text(),
        'position': cols[2].get_text(),
        'height': cols[3].get_text(),
        'weight': cols[4].get_text(),
        'age': cols[5].get_text(),
        'team': cols[6].get('rel'),
        'yos': cols[7].get_text(),
        'pre_draf_team': cols[8].get_text(),
        'draf': cols[9].get_text(),
        'nation': cols[10].get_text()
    }
    print(data)
    play.insert_one(data)

pd.DataFrame(list(play.find())).to_csv('play.csv', index=False)

from bs4 import BeautifulSoup
import requests
import pandas as pd
import pymongo

client = pymongo.MongoClient('localhost', 27017)
myapp = client['myapp']
nowplaying = myapp['nowplaying']

url = 'https://movie.douban.com/cinema/nowplaying/shenzhen/'
douban = requests.get(url).text
soup = BeautifulSoup(douban, 'lxml')
images = soup.select(
    '#nowplaying > div.mod-bd > ul > li > ul > li.poster > a > img')
titles = soup.select('#nowplaying > div.mod-bd > ul > li > ul > li.stitle > a')
rates = soup.select('#nowplaying > div.mod-bd > ul > li > ul > li.srating')


for image, title, rate in zip(images, titles, rates):
    data = {
        'image': image.get('src'),
        'title': title.get('title'),
        'rate': rate.get_text().strip()
    }
    print(data)
    nowplaying.insert_one(data)

# movie_df = pd.DataFrame(data) # 用pandas包结构化数据方便直接导出csv格式文件
# movie_df.to_csv('nowplaying.csv', index=False)

# nowplaying.insert_one(data)  # 放入一个列表方便于后续的存储及分析

# print(movies)
# for movie in nowplaying.find():
#   if movie['rate'].isalpha() == False and float(movie['rate']) >= 7.4:
#     print(movie['title'], movie['rate'])

# movie_load = list(nowplaying.find())
movie_df = pd.DataFrame(list(nowplaying.find()))  # DataFrame的数据需列表化
movie_df.to_csv('now.csv', index=False)

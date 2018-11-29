from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
myapp = client['myapp']
movies = myapp['movies']

urls = [
    'https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0, 250, 25)]


def get_info(url):
    _250 = requests.get(url).text
    time.sleep(2)
    soup = BeautifulSoup(_250, 'lxml')
    images = soup.select('a > img')
    titles = soup.select('div.hd > a > span:nth-of-type(1)')
    years = soup.select('div.bd > p:nth-of-type(1)')
    areas = soup.select('div.bd > p:nth-of-type(1)')
    cates = soup.select('div.bd > p:nth-of-type(1)')
    rates = soup.select('span.rating_num')
    mans = soup.select('div.star > span:nth-of-type(4)')
    critics = soup.select('span.inq')

    for image, title, year, area, cate, rate, man, critic in zip(
            images, titles, years, areas, cates, rates, mans, critics):
        data = {
            'image': image.get('src'),
            'title': title.get_text(),
            'year': list(year.stripped_strings)[-1].split('/')[-3].strip(),
            'area': list(area.stripped_strings)[-1].split('/')[-2].strip().split()[0],
            'cate': list(cate.stripped_strings)[-1].split('/')[-1].strip().split()[0],
            'rate': rate.get_text(),
            'man': man.get_text()[:-3],
            'critic': critic.get_text(),
        }
        print(data)
        movies.insert_one(data)


for url in urls:
    get_info(url)
# get_info('https://movie.douban.com/top250?start=0&filter=')

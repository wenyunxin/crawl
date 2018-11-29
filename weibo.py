# 过程编程
from selenium import webdriver
import time

url = 'https://weibo.com/1560906700/H4KM8t1fS?from=page_1005051560906700_profile&wvr=6&mod=weibotime&type=comment#_rnd1543387021938'


def start_chrome():
    driver = webdriver.Chrome(
        executable_path='./chromedriver')  # webdriver.Chrome方法
    driver.start_client()
    return driver


def get_info():
    sel = 'span > span.S_line1> span> em:nth-child(2)'
    elems = driver.find_elements_by_css_selector(sel)  # 利用webdriver库的方法获取元素
    return [el.text for el in elems[1:]]  # 列表解析式获取所需数据


while True:
    driver = start_chrome()
    driver.get(url)
    time.sleep(6)
    info = get_info()
    repo, commi, likes = info  # 列表对象赋名字
    if int(repo) > 20:
        print('reposts is over ' + repo)
        print(f'reposts is over {repo}')  # f-string
        break
    else:
        print('Nothing')

print('Done')

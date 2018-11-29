
import requests
import time
import webbrowser # 引入Python内置库


info = requests.get(
    'https://api.github.com/repos/wenyunxin/my_page').json()  # 获取的数据字典化
last_update = '2018-11-27T06:18:32Z'
cur_update = info['updated_at']

while True:
    if last_update < cur_update:
        webbrowser.open('https://www.github.com/wenyunxin/my_page')
    time.sleep(60 * 60 * 24)

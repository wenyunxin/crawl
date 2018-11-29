from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import time
import sys


class Spider:

    def __init__(self, index_url):
        self.index_url = index_url
        self.raw_htmls = []
        self.boot()

    def boot(self):
        self.chrome = Chrome(executable_path='./chromedriver')
        self.chrome.start_client()
        self.check_cookie()

    def check_cookie(self):
        from goods import cookie_list
        if cookie_list:
            self.chrome.get(self.index_url)
            time.sleep(5)
            self.chrome.delete_all_cookies()
            print('clear, wait for loading..')
            time.sleep(5)
            for c in cookie_list:
                self.chrome.add_cookie(c)
                print('---')
            print('Done')
        else:
            print('add cookie first')
            sys.exit()

    def crawl(self, target_url):
        self.chrome.get(target_url)
        print('wait for webpage loading..')
        time.sleep(5)
        self.raw_htmls.append(self.chrome.page_source)


class Parser:
    def __init__(self, html_list):
        self.html_list = html_list
        self.raw_post = []
        self.parse()

    def parse(self):
        for html in self.html_list:
            soup = BeautifulSoup(html, 'html.parser')
            detail_sel = '.WB_detail'
            detail_elems = soup.select(detail_sel)
            for detail in detail_elems:
                content = detail.get_text()
                clean_content = content.replace(' ', '').replace('\n', '')
                self.raw_post.append(clean_content)
            print(self.raw_post)

    def save_csv(self):
        with open('./storage.csv', 'a+') as f:
            for p in self.raw_post:
                f.write(p)
                f.close()
            print('finish')


s = Spider(index_url='https://www.weibo.com')
s.crawl(target_url='https://www.weibo.com/fav')
p = Parser(s.raw_htmls)
p.save_csv()

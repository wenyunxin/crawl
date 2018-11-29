import requests


def get_names():
    print('Separate each name with space')
    names = input()
    return names.split()

# 主要是查询api接口url的参数使用


def get_item(names):
    for name in names:
        # 先用json()方法字典化获取的数据
        item = requests.get(
            'https://api.github.com/search/repositories?q='+name).json()['items'][0]
        stars = item['forks_count']
        forks = item['stargazers_count']
        ecosys = requests.get(
            'https://api.github.com/search/repositories?q=topic:'+name).json()['total_count']
        print(name+': '+'Stars:'+str(stars)+' Forks:' +
              str(forks) + ' Ecosys:' + str(ecosys))
    return


names = get_names()
get_item(names)

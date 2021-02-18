import time
import requests
from bs4 import BeautifulSoup
import random


# 去重
def getUniqueItems(iterable):
    seen = set()
    result = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


# 获取html,获取用户名字
def start(list1, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/88.0.4324.182 Safari/537.36 '
    }
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    r.enconding = "utf-8"
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')  # 文档对象
    for i in soup.find_all('a'):
        i = str(i)
        if 'people' in i:
            k = i.split('/')
            list1.append(k[4])


if __name__ == "__main__":
    # 选取了三部春节档电影
    list1 = []  # 你好，李焕英
    list2 = []  # 唐人街探案3
    list3 = []  # 刺杀小说家
    temp = []  # 暂存
    cnt = []  # 计数器
    page = [175, 255, 100]  # 页数
    info = ['34841067', '27619748', '26826330']
    for k in range(0, 3):
        for i in range(0, page[k]):
            print('第', i + 1, '页')
            start(temp, r'https://movie.douban.com/subject/' + info[k] + '/reviews?start=' + str(
                i * 2) + '0')
            time.sleep(random.randint(5, 10))
        temp = getUniqueItems(temp)
        cnt.append(len(temp))
        if k == 0:
            list1 = temp
        elif k == 1:
            list2 = temp
        elif k == 2:
            list3 = temp
        print(f'第{k + 1}次完成，抓取名字个数为{cnt[k]}')
        temp = []
    repeat = []
    for i in list1:
        if i in list2:
            if i in list3:
                repeat.append(i)
    count = len(repeat)
    result = count/cnt[1]
    print('重合度: {:.2%}'.format(result))

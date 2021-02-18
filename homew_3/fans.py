import requests
import datetime
import time
import matplotlib.pyplot as plt


def fans(mid):
    mid = str(mid)
    url = "https://api.bilibili.com/x/relation/stat?vmid=" + mid + "&jsonp=jsonp"
    result = requests.get(url)
    information = eval(result.text)
    num = str(information['data']['follower'])
    return num


if __name__ == "__main__":
    mid = input("爬谁啊兄弟：")
    mid = int(mid)
    temp = input('间隔时间：')
    temp = int(temp)
    count = input("请输入获取次数：")
    count = int(count)
    Time = []
    follower_number = []
    for i in range(0, count):
        Time.append(datetime.datetime.now().strftime('%H:%M:%S'))
        follower_number.append(fans(mid))
        time.sleep(temp)
    plt.plot(Time, follower_number)
    # plt.xticks(rotation=90)  # 横坐标每个值旋转90度
    plt.xlabel('time')
    plt.ylabel('fans_number')
    plt.show()

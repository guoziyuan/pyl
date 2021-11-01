# coding="utf-8"

"""
协程 使用实例

同时访问多个网页，输出返回值得长度

"""

from urllib.request import urlopen
import gevent
from gevent import monkey

monkey.patch_all()


# 访问网页函数
def downlaod(url):
    print("start download :" + url)
    # 网络请求是耗时操作
    try:
        response = urlopen(url)
        data = response.read()
        print('%d bytes received from %s.' % (len(data), url))
    except:
        print("download error")


if __name__ == "__main__":
    webs = ["https://www.baidu.com", "https://www.sina.com", "https://www.163.com"]
    tasks = []
    for url in webs:
        tasks.append(gevent.spawn(downlaod, url))
    gevent.joinall(tasks)

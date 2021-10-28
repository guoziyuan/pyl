# coding="utf-8"
"""
tcp编程

"""
# 客户端

import socket

if __name__ == "__main__":
    # 创建socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接
    s.connect(("www.baidu.com", 80))
    # 发送数据:
    s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
    print("send data")
    # 接收数据
    buffer = []
    while True:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)

    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    # 把接收的数据写入文件:
    with open('baidu.html', 'wb') as f:
        f.write(html)
    s.close()



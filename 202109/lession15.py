# coding="utf-8"

# 服务端

import socket
import threading
import time

if __name__ == "__main__":

    # 获得对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口
    s.bind(("127.0.0.1", 9999))
    # 开始监听, 参数表示等待连接的最大数量
    s.listen(5)


    def tcplink(sock, addr):
        sock.send(b'welcome')
        while True:
            data = sock.recv(1024)
            time.sleep(1)
            if not data or data.decode('utf-8') == 'exit':
                break
            sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))


    while True:
        sock, addr = s.accept()
        # 创建线程处理连接
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()

    sock.close()
    print('Connection from %s:%s closed.' % addr)

# coding="utf-8"

# udp 编程， 不同于tcp监听（listener），使用绑定（bind）
# 服务端
import socket

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口
    s.bind(("127.0.0.1", 9999))
    print("bind 9999")
    while True:
        # recvfrom 返回数据和客户端的地址与端口 ，应该开启线程接收
        data, addr = s.recvfrom(1024)
        print('Received from %s:%s.' % addr)
        # 发送数据到客户端
        s.sendto(b'Hello, %s!' % data, addr)
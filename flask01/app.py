from flask import Flask

import settings

app = Flask(__name__)
# 加载配置
app.config.from_object(settings)

print(app.config)
@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':

    # 默认端口是5000，可以设置host和port
    # 默认host是127.0.0.1，只能本机访问，设置成0.0.0.0，可以被外网访问
    app.run()

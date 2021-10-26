'''
mysql数据库
'''
import mysql.connector
from mysql.connector.constants import SQLMode
import re
print(mysql.connector.apilevel)
print(mysql.connector.paramstyle)

# 判断表是否存在
def table_exit(cursor, table) :
    sql = "show tables;"
    cursor.execute(sql)
    tables = [cursor.fetchall()]
    print(tables)
    table_list = re.findall('(\'.*?\')', str(tables))
    table_list = [re.sub("'",'',each) for each in table_list]

    if table in table_list:
        return 1
    else:
        return 0


# 连接数据库
conn = mysql.connector.connect(user = "root", password = "password", database = "gzy")
# 获得游标
cursor = conn.cursor()

if not table_exit(cursor, "lession"):
    # 执行建表语句
    print("create table lession")
    cursor.execute(
        "create table lession(\
            id varchar(20) primary key,\
            name varchar(50));"
    )

# 插入数据
sql1 = "insert into lession(id, name) values(%s, %s);"
cursor.execute(sql1, ["001", "liming"])
cursor.execute(sql1, ["002", "wangmei"])
cursor.execute(sql1, ["003", "sanqi"])
# 提交操作，不提交，前面操作不生效
conn.commit()

# 查询数据
sql2 = "select * from lession;"
cursor.execute(sql2)
result = cursor.fetchall()
for x in result:
    print(x)
cursor.close()
conn.close()
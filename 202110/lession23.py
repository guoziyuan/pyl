'''
创建数据表
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

if not table_exit(cursor, "math"):
    # 执行建表语句
    print("create table math")
    sql = "create table math(\
        id varchar(20) primary key,\
        name varchar(50),\
        ms int);"

    cursor.execute(sql)
cursor.close()
conn.close()
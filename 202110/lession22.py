'''
ORM ,对象与数据库表映射
'''

from sqlalchemy import Column, create_engine,String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import true

#数据库映射基类
Base = declarative_base()

# 数据库表映射类
class Math(Base):
    __tablename__="math"
    id = Column(String(20), primary_key=true)
    name = Column(String(50))
    ms = Column(Integer)
#固定引擎连接
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/gzy')
DBSession = sessionmaker(bind=engine)
session = DBSession()

# lilizong = Math(id = "001", name = "李莉总", ms = 10)
# zhaosi = Math(id = "002", name = "赵四", ms = 90)
# wangwu = Math(id = "003", name = "王五", ms = 88)
# session.add(lilizong)
# session.add(zhaosi)
# session.add(wangwu)
# session.commit()

#查询所有
users = session.query(Math.id, Math.name, Math.ms).all()
for x in users:
    print(x)
session.close()
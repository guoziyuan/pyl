'''
re模块与正则表达式
【abc]   表示a、b、c中任意一个

[pP]ython  表示Python 或者 python
[0~9a~z] 
'''

import re
data = "andiandifnirnfandcaiu3294jidji@nxne4i"
s = "[abc]a"

#寻找第一个符合的
print(re.search(s, data))
#从头匹配
print(re.match(s, data))
#分割
print(re.split(s, data))
#寻找所有，返回list
print(re.findall(s, data))

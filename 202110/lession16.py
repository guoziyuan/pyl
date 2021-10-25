'''
栈 和 队列
'''

# 栈，用list就可以
a = [1, 2, 3, 4]
print(a)
a.append(5)
print(a)
a.pop()
print(a)


#队列
from collections import deque
b = deque(a)
print(b)

b.popleft()
print(b)
b.append(5)
print(b)
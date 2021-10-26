'''
反转单链表
'''

# 定义节点

class Node() :

    def __init__(self, value) -> None:
        self.value = value
        self.next = None

# 定义单链表
header  = Node(0)
node1 = Node(1)
header.next = node1
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3

def reverseLinkNode(pHeader):
    if not pHeader or not pHeader.next:
       return pHeader
    #前一个指针
    pre = None
    #当前指针
    cur = pHeader
    while cur :
        #保存当前节点 的下一个节点
        tmp = cur.next
        # 当前节点next指向前一个节点
        cur.next = pre
        #前一个指针移动到当前节点位置
        pre = cur
        # 当前节点后移一位，相当于在下一个节点，而下一个节点保存在tmp中
        cur = tmp
    return pre

def printLinkNode(pHeader) :
    while pHeader:
        print(pHeader.value, end = "")
        pHeader = pHeader.next

printLinkNode(header)
print("\n------------")
printLinkNode(reverseLinkNode(header))
"""
list 列表常用功能练习
"""

# 定义这个列表，并用变量接收它
mylist = [21, 25, 21, 23, 22, 20]
print(mylist)

# 追加一个数字 31，到列表的尾部
mylist.append(31)
print(mylist)

# 追加一个新列表 [29, 33, 30]，到列表的尾部
mylist2 = [29, 33, 30]
mylist.extend(mylist2)
print(mylist)

# 取出第一个元素
print(f"第一个元素是：{mylist[0]}")

# 取出最后一个元素
print(f"最后一个元素是：{mylist[-1]}")

# 查找元素 31，在列表中的下标位置
print(f"查找元素 31 在列表中的下标位置为：{mylist.index(31)}")
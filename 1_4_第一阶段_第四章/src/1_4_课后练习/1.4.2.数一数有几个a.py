"""
数一数有几个 a
"""
# 统计如下字符串中，有多少个字母 a
name = "itheima is a brand of itcast"

# 定义一个变量，用来统计有多少个 a
num = 0

# for 循环统计
# for 临时变量 in 被统计的数据:
for i in name:
    if i == 'a':
        num += 1

print(f"{name} 中共含有：{num} 个字母 a")
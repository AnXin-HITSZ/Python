"""
信息去重
"""

my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']
print(f"有列表：{my_list}")

# 定义一个空集合
my_set = set()
# 通过 for 循环遍历列表
for element in my_list:
    # 在 for 循环中将列表的元素添加至集合
    my_set.add(element)

# 最终得到元素去重后的集合对象，并打印输出
print(f"存入集合后结果：{my_set}")
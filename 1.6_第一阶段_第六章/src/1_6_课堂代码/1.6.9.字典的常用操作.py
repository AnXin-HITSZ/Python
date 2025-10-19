"""
演示字典的常用操作
"""

my_dict = {"周杰轮": 99, "林俊节": 88, "张学油": 77}

# 新增元素
my_dict["张信哲"] = 66
print(f"字典经过新增元素后，结果：{my_dict}")

# 更新元素
my_dict["周杰轮"] = 33
print(f"字典经过更新后，结果：{my_dict}")

# 删除元素
score = my_dict.pop("周杰轮")
print(f"字典中被移除了一个元素，结果：{my_dict}，周杰轮的考试分数是：{score}")

# 清空元素
my_dict.clear()
print(f"字典被清空了，内容是：{my_dict}")

# 获取全部的 key
my_dict = {"周杰轮": 99, "林俊节": 88, "张学油": 77}
keys = my_dict.keys()
print(f"字典的全部 keys 是：{keys}")

# 遍历字典
# 方式 1：通过获取到全部的 key 来完成遍历
for key in keys:
    print(f"字典的 key 是：{key}")
    print(f"字典的 value 是：{my_dict[key]}")
# 方式 2：直接对字典进行 for 循环，每一次循环都是直接得到 key
for key in my_dict:
    print(f"2字典的 key 是：{key}")
    print(f"2字典的 value 是：{my_dict[key]}")

# 统计字典内的元素数量：len() 函数
num = len(my_dict)
print(f"字典中的元素数量有：{num} 个")
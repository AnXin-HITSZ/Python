"""
元组的基本操作
"""

# 定义一个元组
t = ('周杰轮', 11, ['football', 'music'])
# 输出初始元组
print(f"该学生的初始信息为：{t}")

# 查询其年龄所在的下标位置
age_index = t.index(11)
print(f"该学生信息中年龄所在的下标位置为：{age_index}")
# 查询学生的姓名
name = t[0]
print(f"该学生的姓名为：{name}")
# 删除学生爱好中的 football
del t[2][0]
print(f"删除学生爱好中的 football，修改后的学生信息为：{t}")
# 增加爱好：coding 到爱好 list 内
t[2].append('coding')
print(f"增加爱好 coding 到爱好 list 内，修改后的学生信息为：{t}")
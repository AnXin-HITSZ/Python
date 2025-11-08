"""
列表嵌套
"""
import random

# 教室列表
classrooms = [[], [], []]
# 讲师列表
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# 遍历讲师列表
for teacher in teachers:
    # 将讲师随机分配到 3 个教室中
    classroom = random.randint(1, 3)
    classrooms[classroom - 1].append(teacher)
# 输出分配结果
print(f"8 名讲师的随机分配结果为：{classrooms}")

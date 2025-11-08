"""
幸运数字 6
"""
# 输入任意数字
num = int(input("请输入任意数字："))
# 生成 nums 列表
nums = []
for i in range(1, num + 1):
    nums.append(i)
# 创建新列表
lucky = []
# 从中选取幸运数字（能够被 6 整除）
for i in nums:
    if i % 6 == 0:
        lucky.append(i)
# 打印原始列表 nums
print(f"原始列表 nums = {nums}")
# 打印最终列表 lucky
print(f"最终列表 lucky = {lucky}")

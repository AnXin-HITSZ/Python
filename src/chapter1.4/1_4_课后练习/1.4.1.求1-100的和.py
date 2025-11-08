"""
求 1 - 100 的和
"""
i = 1
numSum = 0
while i <= 100:
    numSum = numSum + i
    i += 1

print(f"1 - 100 累加的和是：{numSum}")
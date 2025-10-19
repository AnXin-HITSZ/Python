"""
for 循环打印九九乘法表
"""

# 通过外层循环控制行数
for i in range(1, 10):
    # 通过内层循环控制每一行的数据
    for j in range(1, i + 1):
        print(f"{j} * {i} = {j * i}\t", end='')

    # 外层循环可以通过 print 输出一个回车符
    print()
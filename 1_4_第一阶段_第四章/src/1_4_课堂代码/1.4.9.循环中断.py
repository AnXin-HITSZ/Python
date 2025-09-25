"""
演示循环语句的中断控制：break 和 continue
"""

# 演示循环中断语句 continue
# for i in range(1, 6):
#     print("语句 1")
#     continue
#     print("语句 2")

# 演示 continue 的嵌套应用
# for i in range(1, 6):
#     print("语句 1")
#     for j in range(1, 6):
#         print("语句 2")
#         continue
#         print("语句 3")
#
#     print("语句 4")

# 演示循环中断语句 break
# for i in range(1, 101):
#     print("语句 1")
#     break
#     print("语句 2")
#
# print("语句 3")

# 演示 break 的嵌套应用
for i in range(1, 6):
    print("语句 1")
    for j in range(1, 6):
        print("语句 2")
        break
        print("语句 3")

    print("语句 4")
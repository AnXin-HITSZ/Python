"""
演示 if elif else 多条件判断语句的使用
"""
# 通过 if 判断，可以使用多条件判断的语法
# 第一个条件就是 if
if int(input("请输入你的身高（cm）：")) < 120:
    print("身高小于 120cm，可以免费。")
elif int(input("请输入你的 VIP 等级（1 - 5）：")) > 3:
    print("VIP 级别大于 3，可以免费。")
elif int(input("请告诉我今天几号：")) == 1:
    print("今天是 1 号免费日，可以免费。")
else:
    print("不好意思，条件都不满足，需要买票 10 元。")
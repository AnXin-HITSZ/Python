"""
猜猜心里数字
"""
# 定义一个变量数字
num = 10

# 通过键盘输入获取猜想的数字，通过多次 if 和 elif 的组合进行猜想比较
if int(input("请输入第一次猜想的数字：")) == num:
    print("恭喜第一次就猜对了呢！")
elif int(input("不对，再猜一次：")) == num:
    print("猜对了！")
elif int(input("不对，再猜最后一次：")) == num:
    print("恭喜，最后一次机会，你猜对了！")
else:
    print(f"Sorry，全部猜错啦，我想的是：{num}")
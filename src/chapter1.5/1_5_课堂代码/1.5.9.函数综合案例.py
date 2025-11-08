"""
演示函数综合案例开发
"""

# 定义全局变量 money、name
money = 5000000
name = None
# 要求客户输入姓名
name = input("请输入您的姓名：")

# 定义查询函数
def query(show_header):
    if show_header:
        print("--------------- 查询余额 ---------------")
    print(f"{name}，您好，您的余额剩余：{money} 元")
# 定义存款函数
def saving(num):
    global money    # money 在函数内部定义为全局变量
    money += num
    print("--------------- 存款 ---------------")
    print(f"{name}，您好，您存款 {num} 元成功。")

    # 调用 query 函数查询余额
    query(False)
# 定义取款函数
def get_money(num):
    global money
    money -= num
    print("--------------- 取款 ---------------")
    print(f"{name}，您好，您取款 {num} 元成功。")
# 定义主菜单函数
def main():
    print("--------------- 主菜单 ---------------")
    print(f"{name}，您好，欢迎来到黑马银行 ATM。请选择操作：")
    print("查询余额\t[输入 1]")
    print("存款\t[输入 2]")
    print("取款\t[输入 3]")
    print("退出\t[输入 4]")
    return input("请输入您的选择：")

# 设置无限循环，确保程序不退出
while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query(True)
        continue    # 通过 continue 继续下一次循环，一进来就是回到了主菜单
    elif keyboard_input == "2":
        num = int(input("您想要存多少钱？请输入："))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("您想要取多少钱？请输入："))
        get_money(num)
        continue
    else:
        print("程序退出啦")
        break   # 通过 break 退出循环
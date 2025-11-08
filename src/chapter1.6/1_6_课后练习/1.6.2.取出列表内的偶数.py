"""
取出列表内的偶数
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def list_while_func():
    my_list_new = []
    index = 0
    while index < len(my_list):
        if my_list[index] % 2 == 0:
            my_list_new.append(my_list[index])
        index += 1

    print(f"通过 while 循环，从列表：{my_list} 中取出偶数，组成新列表：{my_list_new}")

def list_for_func():
    my_list_new = []
    for element in my_list:
        if element % 2 == 0:
            my_list_new.append(element)

    print(f"通过 for 循环，从列表：{my_list} 中取出偶数，组成新列表：{my_list_new}")

list_while_func()
list_for_func()
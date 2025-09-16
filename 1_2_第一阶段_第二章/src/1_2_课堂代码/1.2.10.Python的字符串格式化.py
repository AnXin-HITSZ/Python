# 通过占位的形式，完成拼接
name = "黑马程序员"
message = "学 IT 来：%s" % name
print(message)

# 通过占位的形式，完成数字和字符串的拼接
class_num = 57
avg_salary = 16781
message = "Python 大数据学科，北京 %s 期，毕业平均工资：%s" % (class_num, avg_salary)
print(message)

name = "传智播客"
setup_year = 2006
stock_price = 19.99
message = "%s，成立于：%d，我今天的股价是：%f" % (name, setup_year, stock_price)
print(message)


num1 = 11
num2 = 11.345
print("数字 11 宽度限制 5，结果是：%5d" % num1)
print("数字 11 宽度限制 1，结果是：%1d" % num1)
print("数字 11.345 宽度限制 7，小数精度 2，结果是：%7.2f" % num2)
print("数字 11.345 宽度不限制，小数精度 2，结果是：%.2f" % num2)
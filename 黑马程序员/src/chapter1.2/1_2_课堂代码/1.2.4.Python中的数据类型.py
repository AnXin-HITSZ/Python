# 方式 1：使用 print 直接输出类型信息
print(type("黑马程序员"))
print(type(666))
print(type(11.345))
# 方式 2：使用变量存储 type() 语句的结果
string_type = type("黑马程序员")
int_type = type(666)
float_type = type(11.345)
print(string_type)
print(int_type)
print(float_type)
# 方式 3：使用 type() 语句，查看变量中存储的数据类型信息
name = "黑马程序员"
name_type = type(name)
print(name_type)
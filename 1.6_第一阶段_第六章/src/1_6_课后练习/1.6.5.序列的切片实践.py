"""
序列的切片实践
"""

# 定义一个原始字符串
my_str = "万过薪月，员序程马黑来，nohtyP学"
# 对原始字符串进行切片操作
new_my_str = my_str[5:10]
# 对切片所得字符串进行反转
re_new_my_str = new_my_str[::-1]
# 输出处理后的字符串
print(re_new_my_str)

my_str = "万过薪月，员序程马黑来，nohtyP学"

# 倒序字符串，切片取出
result1 = my_str[::-1][9:14]
print(f"方式 1 结果：{result1}")
# 切片取出，然后倒序
result2 = my_str[5:10][::-1]
print(f"方式 2 结果：{result2}")

# split 分隔 "，"，replace 替换 "来" 为空，倒序字符串
result3 = my_str.split("，")[1].replace("来", "")[::-1]
print(f"方式 3 结果：{result3}")
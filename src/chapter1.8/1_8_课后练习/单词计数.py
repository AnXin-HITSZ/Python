"""
单词计数
"""

""" 个人思路 """
"""
# 打开文件
f = open('D:/Learn/Python/src/chapter1.8/word.txt', 'r', encoding='UTF-8')
# 读取文件的全部行
content = f.readlines()

count = 0
for line in content:
    line = line.replace('\n', '')
    line = line.split(' ')
    for word in line:
        if word == 'itheima':
            count = count + 1

print(f"itheima 单词出现的次数为：{count}")
f.close()
"""

""" 参考思路 """

# 打开文件，以读模式打开
f = open('D:/Learn/Python/src/chapter1.8/word.txt', 'r', encoding='UTF-8')
# 方式 1：读取全部内容，通过字符串 count 方法统计 itheima 单词数量
# content = f.read()
# count = content.count("itheima")
# print(f"itheima 在文件中出现了：{count} 次")
# 方式 2：读取内容，一行一行读取
count = 0   # 使用 count 变量来累计 itheima 出现的次数
for line in f:
    words = line.split(" ")
    line = line.strip() # 去除开头和结尾的空格以及换行符
    words = line.split(" ")
    for word in words:
        if word == 'itheima':
            count += 1  # 如果单词是 itheima，进行数量的累加加 1
# 判断单词出现次数并累计
print(f"itheima 出现的次数是：{count}")
# 关闭文件
f.close()

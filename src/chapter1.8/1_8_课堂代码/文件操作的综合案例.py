"""
演示文件操作综合案例：文件备份
"""

# 打开文件得到文件对象，准备读取
fr = open("D:/Learn/Python/src/chapter1.8/bill.txt", "r", encoding="UTF-8")
# 打开文件的得到文件对象，准备写入
fw = open("D:/Learn/Python/src/chapter1.8/bill.txt.bak", "w", encoding="UTF-8")
# for 循环读取文件
for line in fr:
    line = line.strip()
    # 判断内容，将满足的内容写出
    if line.split(",")[4] == "测试":
        continue    # continue 进入下一次循环，这一次后面的内容就跳过了
    # 将内容写出去
    fw.write(line)
    # 由于前面对内容进行了 strip() 的操作，所以要手动的写出换行符
    fw.write("\n")

# close 2 个文件对象
fr.close()
fw.close()  # 写出文件调用 close() 会自动 flush()

"""
演示文件的追加写入
"""

# 打开文件，不存在的文件
# f = open("D:/Learn/Python/src/chapter1.8/test_文件的追加写入.txt", "a", encoding="UTF-8")
# # write 写入
# f.write("黑马程序员")
# # flush 刷新
# f.flush()
# # close 关闭
# f.close()
# 打开一个存在的文件
f = open("D:/Learn/Python/src/chapter1.8/test_文件的追加写入.txt", "a", encoding="UTF-8")
# write 写入、flush 刷新
f.write("\n月薪过万")
# close 关闭
f.close()

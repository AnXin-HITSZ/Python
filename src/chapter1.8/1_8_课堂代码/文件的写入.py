"""
演示文件的写入
"""

# 打开文件，不存在的文件，r、w、a
import time

# f = open("D:/Learn/Python/src/chapter1.8/test_文件的写入.txt", "w", encoding="UTF-8")
# # write 写入
# f.write("Hello World!!!")   # 内容写入到内存中
# # flush 刷新
# # f.flush()   # 将内存中积攒的内容，写入到硬盘的文件中
# # time.sleep(600000)
# # close 关闭
# f.close()   # close 方法，内置了 flush 的功能的

# 打开一个存在的文件
f = open("D:/Learn/Python/src/chapter1.8/test_文件的写入.txt", "w", encoding="UTF-8")
# write 写入、flush 刷新
f.write("黑马程序员")
# close 关闭
f.close()

"""
有几个偶数
"""
num = 100
count = 0
for i in range(1, num):
    if i % 2 == 0:
        count += 1

print(f"1 到 {num}（不含 {num} 本身）范围内，有 {count} 个偶数。")
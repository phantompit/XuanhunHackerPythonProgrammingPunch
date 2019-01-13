# break 语句终止
# continue 示循环继续执行下一次迭代
# pass 语句什么也不做 占位符
a = b = 0
while True:
    a += 1
    print("第%s次" % a)
    if a > 9:
        break

# continue
print('continue.....')
for num in range(2,10):
    if(num %2 == 0):
        continue
    print(num)


pass
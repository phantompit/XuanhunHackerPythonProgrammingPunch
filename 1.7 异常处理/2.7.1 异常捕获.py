while True:
    try:
        n = input("请你输入一个整数：")
        n = int(n)
        break
    except ValueError as e:
        print("输入无效数字，请你再次输入",e)
print("输入成功")
import sizeyunsuan
sizeyunsuan.sayhi()
print('This Version is：', sizeyunsuan.version)
while True:
    xuanze = str(input("请你重新选择一个算法\nA.加法\nB.减法\nC.乘法\nD.除法                                                      "))
    if xuanze == ("a") or xuanze == ("A"):
        sizeyunsuan.add()
        break
        
    elif xuanze == ("b") or xuanze == ("B"):
        sizeyunsuan.sub()
        break
    elif xuanze ==("c") or xuanze == ("C"):
        sizeyunsuan.mass()
        break
    elif xuanze ==("d") or xuanze == ("D"):
        sizeyunsuan.cf()
        break
    else:
        print("你输入的内容不在模块列表选项中")
pass
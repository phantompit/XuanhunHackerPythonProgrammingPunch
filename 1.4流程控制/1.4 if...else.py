# -*- coding: UTF-8 -*-
while True:
    a = int(float(input("请你输入一个整数：")))
    if a == 0:
        print(("%d == 0" % a))
    elif a < 0:
        print(("%d < 0" % a))
    else:
        print(("%d > 0" % a))
def sayhi():
    print('四则运算模块')
version = '0.1'
def add():#加法
    he = num1 = num2 = 0
    num1 = int(float(input("请你输入第一个数字:")))
    num2 = int(float(input("请你输入第一个数字:")))
    he = num1 + num2
    print("{}+{}={}".format(num1,num2,he))

def sub():#减法
    he = num1 = num2 = 0
    num1 = int(float(input("请你输入第一个数字:")))
    num2 = int(float(input("请你输入第一个数字:")))
    he = num1 - num2
    print("{}-{}={}".format(num1, num2, he))
def mass():#乘法
    he = num1 = num2 = 0
    num1 = int(float(input("请你输入第一个数字:")))
    num2 = int(float(input("请你输入第一个数字:")))
    he = num1 * num2
    print("{}*{}={}".format(num1, num2, he))
def cf():#除法
    he = num1 = num2 = 0
    num1 = int(float(input("请你输入第一个数字:")))
    num2 = int(float(input("请你输入第一个数字:")))
    he = num1 / num2
    print("{}*{}={}".format(num1, num2, he))
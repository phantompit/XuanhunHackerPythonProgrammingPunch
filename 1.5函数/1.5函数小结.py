# 将1.4节的练习题的实现都封装到函数中，传入不同的参数进行调用测试
# 实现用户输入用户名和密码，当用户名为 seven且密码为123时，显示登陆成功，否则登陆失败！
def login(Username,Password):
    while True:
        Username = str(input("请输入用户名"))
        Password = int(input("请输入密码"))
        if Username == str("seven") and Password == int("123"):
            print("成功登录")
            break
Username = str(input("请输入用户名"))
Password = int(input("请输入密码"))
login(Username,Password)

# 用while循环实现输出2-3+4-5+6.....+100的和
def sum(if1=100):
    i = s1 = c = 0
    while True:
        i += 1
        if i % 2 == 0:
            s1 += i
        else:
            s1 -= i
        if i == int(if1):
            break
    print(s1 + 1)
if1 = int(float(input("请你输入最后的数字：")))
sum(if1)
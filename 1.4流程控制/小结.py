# 使用while循环实现输出2-3+4-5+6.....+100的和
# while True:
#     Username = str(input("请你输入用户名:"))
#     Password = str(input("请你输入密码："))
#     if Username == str("seven") and Password == str("123"):
#         break
#     else:
#         print("登录失败")
# print("登录成功")

# 使用while循环实现输出2-3+4-5+6.....+100的和
i =s1 = c =0
while True:
    i += 1
    if i % 2 == 0:
        s1 += i
    else:
        s1 -= i
    if i == 100:
        break
print(s1 + 1)





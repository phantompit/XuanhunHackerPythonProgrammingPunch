# 默认参数
def say(message, times=1):#定义一个函数名称为say
    print(message * times)#程序块



say('Hello')#只提供了一个message变量的值，没有提供times的值所以取默认参数值

say('World', 5)#提供了两个值，传入给函数，并且调用函数打印World 5遍
# zifu = (input("请你输入："))
# bian = int(input("打印多少遍"))
# say(zifu,bian)

# 只有在形参表末尾的那些参数可以有默认参数值，即你不能在声明函数形参的时候，先声明有默认值的形参而后声明没有默认值的形参。这是因为
# 赋给形参的值是根据位置而赋值的。例如，

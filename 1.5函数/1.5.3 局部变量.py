#局部变量
# 函数定义了形参x，相当于函数的局部变量。在函数调用的时候，传入了外部x，外部x值为50。在函数内部将x值改为2，改变的是局部变量x，外部
# x不受影响，从最后的输出结果可以验证。运行结果如下：
# def func(x):
#     print('x is', x)
#     x = 2
#     print('Changed local x to', x)
# print('局部变量')
# x = 60
# func(x)

# 定义在函数外的变量赋值，那么你就得告诉Python这个变量名不是局部的，而是
# 全局
# 的。我们使用global语句完成这一功能。没有global语句，是不可能为定义在函数外的变量赋值的。例如：
# 访问外部变量
def func2():
    global x      #访问一个外部的全局变量

    print('x is', x)
    x = 2
    print('Changed local x to', x)


print('访问外部变量')
x = 50
func2()
print('Value of x is', x)
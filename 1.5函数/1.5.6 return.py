# return语句用来从一个函数返回，即跳出函数。我们也可选从函数返回一个值。例如：

#return
def maximum(x, y):
    if x > y:
        return x
    else:
        return y
print('')
print(maximum(2, 3))
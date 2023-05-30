def my_func(param):
    param.sort(reverse = True)
    a = tuple(param)
    return a
i = list(map(int,input("Listni toldiring:").split()))
a = my_func(i)
print(a)
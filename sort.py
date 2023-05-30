def my_func(param):
    param.sort(reverse = True)
    a = tuple(param)
    return a
i = list(map(int,input("Listni toldiring:").split()))
res = my_func(i)
print(res)
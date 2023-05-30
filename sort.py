def my_func(param):
    param.sort(reverse = True)
    x = tuple(param)
    return x
i = list(map(int,input("Listni toldiring:").split()))
res = my_func(i)
print(res)
def square(l):
    l = [i ** 2 for i in l]
    return l


def map(fun, l):
    return fun(l)


l = [1, 2, 3, 4]
print(map(square, l))

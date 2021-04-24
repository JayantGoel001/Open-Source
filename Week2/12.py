def even_square(l):
    return [x * x for x in l if x % 2 == 0]


def filter(fun, l):
    return fun(l)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def lensort(l):
    l = sorted(l, key=lambda x: len(x))
    return l


l = list(map(str, input().split()))
print(lensort(l))
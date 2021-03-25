import numpy as np
print(np.__version__)

l = list(map(int, input().split()))

d = {}
for i in l:
    if i not in d:
        d[i] = 0
    d[i] += 1

for key, value in d.items():
    print(key, " : ", value)

print("Number of Characters : ", len(d.keys()))
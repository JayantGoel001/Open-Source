l = list(map(int, input().split()))

d = {}
for i in l:
    if i not in d:
        d[i] = 0
    d[i] += 1

for key, value in d.items():
    if value > 1:
        print(key)

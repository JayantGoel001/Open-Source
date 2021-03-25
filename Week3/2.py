l = input()
d = {
    0: 0,
    1: 0
}
for i in range(len(l)):
    d[int(l[i])] += 1

print("1" * d[1] + "0" * d[0])
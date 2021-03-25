l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

output = []
for i in l1:
    if i in l2:
        output.append(True)
    else:
        output.append(False)

print(output)
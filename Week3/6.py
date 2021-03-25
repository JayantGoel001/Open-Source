l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

output = []
for i in l1:
    if i not in l2 and i not in output:
        output.append(i)

for i in l2:
    if i not in l1 and i not in output:
        output.append(i)

output.sort()
print(output)
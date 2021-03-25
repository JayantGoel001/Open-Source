l = list(map(int, input().split()))
size = int(input())

output = []
for i in range(len(l)):
    if i % size == 0:
        output.append([])
    output[i // size].append(l[i])

print(output)

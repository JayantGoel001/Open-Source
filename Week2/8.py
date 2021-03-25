l = []
with open("helloworld.txt",'r+') as f:
    l = f.readlines()

l = l[::-1]
print(l)
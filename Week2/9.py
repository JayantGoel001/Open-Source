l = []
with open("helloworld.txt",'r+') as f:
    l = f.readlines()

for i in l:
    print(i[::-1],end="")

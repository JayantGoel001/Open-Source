l = []
with open("helloworld.txt", 'r+') as f:
    l = f.readlines()

words = []
characters = 0
for line in l:
    words.extend(line.split(" "))
    characters += len(line)

print("Number of Characters: ", characters)
print("Number of Words: ", len(words))
print("Number of Lines: ", len(l))

text = "hello world"
textlines = ['Hello World1 23576\n', 'How is It Going?\n', "maybe!!! I wouldn't\n"]
filename = "helloworld.txt"

with open(filename, 'w+') as f:
    f.write(text)

with open(filename, 'r+') as f:
    print(f.read())

with open(filename, 'w+') as f:
    f.writelines(textlines)

with open(filename, 'r+') as f:
    print(f.readlines())

def parse_csv(lines, sep=','):
    x = []
    for line in lines:
        x.append(line.split(sep))


with open("hello.csv", 'r+') as f:
    lines = f.readlines()

sep = input("Enter Delimiter")
parse_csv(lines, sep)

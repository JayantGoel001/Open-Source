def parse_csv(lines):
    x = []
    for line in lines:
        x.append(line.split(","))


with open("hello.csv", 'r+') as f:
    lines = f.readlines()
parse_csv(lines)

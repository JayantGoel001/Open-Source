import sys

if len(sys.argv) < 3:
    sys.exit(0)

filename = sys.argv[1]
width = sys.argv[2]

with open(filename, 'r+') as f:
    line = f.readlines()

line = "\n".join(line)

a = [line[i:i + width] for i in range(0, len(line), width)]
print("\n".join(a))

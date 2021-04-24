import collections
import pprint

file_input = input()

with open(file_input, 'r') as info:
    count = collections.Counter(info.read().upper())
    value = pprint.pformat(count)

print(value)

a = file_input.split(".")

if a[1] == "txt":
    print("it is a text file")

elif a[1] == "cpp":
    print("it is a c++ file")

else:
    print("it is a c file")

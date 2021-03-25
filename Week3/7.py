import numpy as np

l = list(map(int, input().split()))
stack = np.column_stack(l)
print(stack)
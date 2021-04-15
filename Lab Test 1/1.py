import numpy as np


def checkArmstrong(num):
    Add = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        Add += digit ** 3
        temp //= 10

    if num == Add:
        return True
    else:
        False


def matrixOperations(A, B):
    # 1

    for i in range(A.shape[0]):
        for j in range(i, A.shape[1]):
            if A[i][j] % 2 != 0:
                A[i][j] *= 2

    # 2
    minEle = np.min(B)
    for i in range(min(B.shape[0], B.shape[1])):
        if checkArmstrong(B[i][i]):
            B[i][i] -= minEle

    # 3
    print("Matrix A:")
    print(A)
    print()

    print("Matrix B:")
    print(B)
    print()

    # 4
    if A.shape[1] == B.shape[0]:
        mul = np.dot(A, B)
    else:
        print("Operation cannot be performed")

    # 5
    print("Multiplication")
    if mul is not None:
        print(mul)


n1, m1 = map(int, input().split())
n2, m2 = map(int, input().split())

A = np.zeros(shape=(n1, m1))
B = np.zeros(shape=(n2, m2))

for i in range(n1):
    for j in range(m1):
        A[i][j] = int(input())

for i in range(n2):
    for j in range(m2):
        B[i][j] = int(input())

matrixOperations(A, B)

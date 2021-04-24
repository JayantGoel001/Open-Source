def triplets(n):
    return [(a, c - a, c) for c in range(2, n) for a in range(1, c // 2 + 1)]


n = int(input())
triplets(n)

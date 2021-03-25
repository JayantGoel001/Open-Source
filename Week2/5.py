def exsort(files):
    files = sorted(files, key=lambda file: file.split(".")[-1])
    return files


files = list(map(str, input().split()))
print(exsort(files))

def mutate(d):
    ret = [d]
    i = 0
    l = len(d)
    alp = map(chr, range(97, 123))

    while i < l:
        cop = d
        ret.append(cop[:i] + cop[i + 1:])
        if i < l - 2:
            ret.append(cop[:i] + cop[i + 1] + cop[i] + cop[i + 2:])
        elif i < l - 1:
            ret.append(cop[:i] + cop[i + 1] + cop[i])
        for x in alp:
            ret.append(cop[:i] + x + cop[i + 1:])

    for x in alp:
        ret.append(d + x)
        ret.append(x + d)
        ret.append(cop[:i] + x + cop[i:])
        i = i + 1

    return ret


print('hefllo' in mutate('hello'))
print('hllo' in mutate('hello'))

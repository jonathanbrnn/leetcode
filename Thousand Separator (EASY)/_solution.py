test = 987


def thousandSeparator(n):
    x = str(n)[::-1]
    x = '.'.join(x[i:i+3] for i in range(0, len(x), 3))
    return x[::-1]

print(thousandSeparator(test))

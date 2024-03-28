"""
O que aconteceria se você chamasse esta função desta forma: recurse(-1, 0)?
"""


def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)


recurse(-1, 0)

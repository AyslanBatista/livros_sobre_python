"""
Como exercício, use o get para escrever a função histogram de forma
mais concisa. Tente eliminar a instrução if.

"""


def histogram(s):
    d = dict()
    for c in s:
        if not d.get(c, 0):
            d[c] = 1
        else:
            d[c] += 1
    return d


h = histogram('brontosaurus')
print(h)

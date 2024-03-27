"""
Altere do_twice para que receba dois argumentos, um objeto de função
e um valor, e chame a função duas vezes, passando o valor como um argumento.
"""


def do_twice(f, v):
    f(v)
    f(v)


def print_spam(a):
    print('spam', a)


value = "alo"
do_twice(print_spam, value)

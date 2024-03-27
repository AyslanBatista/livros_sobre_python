"""
Use a versão alterada de do_twice para chamar print_twice duas vezes,
passando 'spam' como um argumento.
"""


def do_twice(f, v):
    f(v)
    f(v)


def print_spam(a):
    print('spam')


def print_twice(bruce):
    print(bruce)
    print(bruce)


do_twice(print_spam, print_twice('spam'))

import sys

def myfunc(a, b):
    print((a + b)*(a - b))

a, b = map(int, input().split())
myfunc(a, b)
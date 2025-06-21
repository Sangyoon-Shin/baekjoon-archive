import sys
input = sys.stdin.readline

a, b, c = map(int,input().split())

product = 1
while True:
    if c * product > a + (b * product):
        print(product)
        break
    else:
        product += 1

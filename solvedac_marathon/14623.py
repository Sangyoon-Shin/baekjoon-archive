import sys
input = sys.stdin.readline

b1= input()
b2 = input()

ib1 = int(b1, 2)
ib2 = int(b2, 2)

res = bin(ib1 * ib2)
print(res[2:])




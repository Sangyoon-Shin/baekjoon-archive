import sys
input = sys.stdin.readline

l = int(input())
a= int(input())
b = int(input())
c = int(input())
d = int(input())

minimum = 0
kmin, mmin = 0, 0
if a % c == 0:
    kmim = a // c
else:
    kmin = a // c + 1

if b % d == 0:
    mmin = b // d
else:
    mmin = b // d + 1
    
print(l - max(kmin, mmin))
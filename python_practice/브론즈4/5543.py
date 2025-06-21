import sys

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

list = [a + d - 50, a + e - 50, b + d - 50, b + e - 50, c + d - 50, c + e - 50]
print(min(list))
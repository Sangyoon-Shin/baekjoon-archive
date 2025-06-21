import sys
from math import ceil

input = sys.stdin.readline

n = int(input())
size = list(map(int, input().split()))

t, p = map(int, input().split())

package = sum([ceil(i / t) for i in size])

print(package)
a, b = divmod(n, p)
print(a, b)
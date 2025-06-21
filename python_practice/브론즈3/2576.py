import sys
input = sys.stdin.readline

odd = []

oddsum = 0
for i in range(7):
    n = int(input())
    if n % 2 == 1:
        odd.append(n)
        oddsum += n

if len(odd) == 0:
    print(-1)
else:
    print(oddsum)
    print(min(odd))

import sys
input = sys.stdin.readline

consumtion = []

t = int(input())
for i in range(t):
    n = int(input())
    for j in range(n):
        name, amount = input().strip().split()
        consumtion.append((name, int(amount)))

    consumtion.sort(key=lambda x:(-x[1]))
    print(consumtion[0][0])

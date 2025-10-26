import sys
input = sys.stdin.readline

n = int(input())
weight = []
for i in range(n):
    weight.append(int(input()))

weight.sort(reverse=True)
maximum = weight[0]

for i in range(1, n):
    if maximum < weight[i] * (i + 1):
        maximum = weight[i] * (i + 1)

print(maximum)  




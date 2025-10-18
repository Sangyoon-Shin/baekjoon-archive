import sys
input = sys.stdin.readline

maximum = 0
n = int(input())
tree = list(map(int, input().split()))

for i in range(len(tree)):
    if tree[i] - (len(tree) - 1 - i)  - 1> maximum:
        maximum = tree[i] - (len(tree) - 1 - i) - 1

print(maximum)
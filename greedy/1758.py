import sys
input = sys.stdin.readline

# 팁을 가장 많이 주려고 했던 애들을 맨 앞에 세우면 됨
n = int(input())
line = []

for i in range(n):
    line.append(int(input()))

line.sort(reverse=True)
maximum = 0

for i in range(len(line)):
    if line[i] - i >= 0:
        maximum += line[i] - i
    else:
        continue

print(maximum)
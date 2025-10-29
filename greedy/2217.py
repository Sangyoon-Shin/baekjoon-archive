import sys
input = sys.stdin.readline

n = int(input())
weight = []
for i in range(n):
    weight.append(int(input()))

weight.sort(reverse=True)
maximum = weight[0]

# 내림차순 정렬을 한 거기 때문에, weight[i] 이전까지의 로프들은 무조건 weight[i]만큼 들 수 있음. 
for i in range(1, n):
    if maximum < weight[i] * (i + 1):
        maximum = weight[i] * (i + 1)

print(maximum)  




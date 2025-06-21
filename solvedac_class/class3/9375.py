import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    category = {}
    for k in range(n):
        clo, cat = map(str, input().strip().split())
        if cat not in category.keys():
            category[cat] = 1
        else:
            category[cat] += 1

    res = 1
    for key in category.keys():
        res = res * (category[key] + 1) # category[key]는 그 종류 의상 선택할 수 있는 가짓수. 착용안하는 경우도 있으니까 + 1
    res = res - 1 # 모든 의상을 착용안 한 한가지 case는 빼줘야함.
    print(res)


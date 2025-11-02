import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    price = list(map(int, input().split()))
    # 맨 뒤에서부터 기준값을 정해주면서 이 값이 현재가보다 크면 무조건 이득이므로 total에 더해주기
    # 작거나 같은 경우에는 그 기준값에 팔아도 이득이 아니니까 현재가를 기준값으로 업데이트
    # 뒤에서부터 거꾸로 순회하는게 핵심이었다.
    tmp = price[-1]
    total = 0
    for j in range(len(price) - 2, -1, -1):
        if tmp > price[j]:
            total += tmp - price[j]
        else:
            tmp = price[j]
    print(total)


import sys
input = sys.stdin.readline

n, m = map(int, input().split())

sixarr = []
onearr = []
for i in range(m):
    six, one = map(int, input().split())
    sixarr.append(six)
    onearr.append(one)

minsix = min(sixarr)
minone = min(onearr)

price = 0

while True:
    if n <= 0:
        break
    elif n >= 6: # n이 6 이상일땐 6개 * 낱개짜리랑 6개 묶음 비교. 6개 묶음이 더 비싸면 6개 낱개로 사기
        if minsix > 6 * minone:
            price = price + (6 * minone)
            n = n - 6
        elif minsix <= 6 * minone:
            price = price + minsix
            n = n - 6
    elif n < 6: # n이 6보다 작으면 1 ~ 5개 남았을 때. 이거는 남은개수 X 낱개가격이랑 6개 묶음 가격이랑 비교
        if minsix > n * minone:
            price = price + (n * minone)
            n = n -6
        elif minsix <= n * minone:
            price = price + minsix
            n = n - 6

print(price)




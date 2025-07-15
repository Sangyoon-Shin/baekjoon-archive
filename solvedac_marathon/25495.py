import sys
input = sys.stdin.readline

n = int(input())
phone = list(map(int, input().split()))

usebat = 0 # 이번에 소모되는 배터리
bat = 0 # 누적 배터리
prev = 0 # 이전 번호
cur = 0 # 현재 번호

for i in phone:
    cur = i
    if cur != prev: # 현재번호랑 이전번호랑 다르면
        usebat = 2 # 2를 소모해야함
        bat += usebat
        prev = cur
        if bat >= 100: # 더했는데 100 이상이면 0으로 초기화
            bat = 0
            prev = 0
    else:
        usebat *= 2 # 이전번호와 같으면 기존에 추가된 값의 2배를 더해줘야함
        bat += usebat
        prev = cur
        if bat >= 100:
            bat = 0
            prev = 0

print(bat)

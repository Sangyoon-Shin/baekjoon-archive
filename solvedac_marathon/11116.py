import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    left = list(map(int, input().split()))
    right = list(map(int, input().split()))

    cnt = 0
    # 왼쪽 앞바퀴 <-> 오른쪽 앞바퀴, 왼쪽 뒷바퀴 <-> 오른쪽 뒷바퀴가 각각 매칭되면 차 한 대 지나간 것.
    for time in left:
        if time + 1000 in right:
            if time + 500 in left and time + 1500 in right:
                cnt += 1
    
    print(cnt)
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for i in range(t):
    commandlist = deque()
    command = input().strip()
    commandlist.extend(command)
    n = int(input())
    k = input().strip()
    k = k[1:-1]
    if len(k) >= 1:
        value = deque(map(int, k.split(',')))
    else:
        value = deque()
    
    revflag = False
    flag = 0
    while len(commandlist) > 0:
        com = commandlist.popleft()
        if com == 'R':
            ## value.reverse() -> O(n), 근데 모든 명령이 뒤집기면 시간 복잡도 MN
            revflag = not revflag
        elif com == 'D':
            if len(value) == 0:
                print('error')
                flag = 1
                break
            elif revflag == False: # 이게 false인건 그대로 맨 왼쪽거 뽑으면 되는 경우
                value.popleft()
            elif revflag == True:
                value.pop()

    value = list(map(str, value))
    
    if flag == 0:
        if revflag == True:
            value.reverse()
        print('[', end='')
        print(','.join(value), end ='')
        print(']')
    

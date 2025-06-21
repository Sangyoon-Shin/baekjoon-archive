import sys
from collections import deque
input = sys.stdin.readline

# n = int(input())
# deck = deque()
# rollback = [[]]
# act = 0

# # for문 O(n), append로 복사본 만들때 O(k) -> O(nk) 최악 O(n^2)
# for i in range(n):
#     command = input().split()
#     if command[0]=='push':
#         deck.append(int(command[1]))
#         act += 1
#         rollback.append(list(deck))
    
#     elif command[0]=='pop':
#         deck.pop()
#         act += 1
#         rollback.append(list(deck))
        
#     elif command[0]=='restore':
#         idx = int(command[1])
#         deck = deque(rollback[idx])

#     elif command[0] =='print':
#         if len(deck) == 0:
#             print('0')
#         else:
#             print(sum(deck))


# 각각의 act를 기록해두자
n = int(input())
sumlist = [0]*(n + 1)
toplist = [0]*(n + 1)
prevlist = [0]*(n + 1)

cur = 0

for i in range(1, n + 1):
    command = input().split()
    if command[0] == 'push':
        value = int(command[1])
        sumlist[i] = sumlist[cur] + value
        toplist[i] = value
        prevlist[i] = cur
        cur = i

    elif command[0] == 'pop':
        if cur == 0:
            sumlist[i] = 0
            toplist[i] = 0
            prevlist[i] = 0
            cur = i
        else:
            prev = prevlist[cur]
            sumlist[i] = sumlist[prev]
            toplist[i] = toplist[prev]
            prevlist[i] = prevlist[prev]
            cur = i

    elif command[0] == 'restore':
        act = int(command[1])
        if(act == 0):
            sumlist[i] = 0
            toplist[i] = 0
            prevlist[i] = 0
            cur = i
        else:
            sumlist[i] = sumlist[act]
            toplist[i] = toplist[act]
            prevlist[i] = prevlist[act]
            cur = i

    elif command[0] == 'print':
        if cur == 0:
            print(0)
        else:
            print(sumlist[cur])







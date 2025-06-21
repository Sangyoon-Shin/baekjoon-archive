import sys
from collections import deque
input = sys.stdin.readline

string = list(input().strip())

cursorleft = []
cursorright = deque()

for i in string:
    cursorleft.append(i)

n = int(input())
for i in range(n):
    command = list(input().split())
    if command[0] == 'P':
        cursorleft.append(command[1])
    elif command[0] == 'B':
        if len(cursorleft) == 0:
            pass
        else:
            cursorleft.pop()
    elif command[0] == 'L':
        if len(cursorleft) == 0:
            pass
        else:
            cursorright.appendleft(cursorleft.pop())
    elif command[0] == 'D':
        if len(cursorright) == 0:
            pass
        else:
            cursorleft.append(cursorright.popleft())

ans = cursorleft + list(cursorright)
for i in ans:
    print(i, end='')




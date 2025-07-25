import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()

for i in range(n):
    command = input().split()
    if command[0] == 'push':
        x = int(command[1])
        q.append(x)

    elif command[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
        
    elif command[0] == 'size':
        print(len(q))

    elif command[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])

    elif command[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[len(q) - 1])
import sys
from collections import deque
input = sys.stdin.readline

s = list(input())

stack = deque()
res = []

flag = 0
for i in s:
    if i == ' ' and flag == 0:
        while len(stack) != 0:
            res.append(stack.pop())
        res.append(' ')
    elif i == ' ' and flag == 1:
        stack.append(' ')
    elif i == '<':
        flag = 1
        while len(stack) != 0:
            res.append(stack.pop())
        stack.append(i)
    elif i == '>':
        flag = 0
        while len(stack) != 0:
            res.append(stack.popleft())
        res.append('>')
    elif (i >= 'a' and i <= 'z') or (i >= '0' and i <= '9'):
        stack.append(i)
    elif i == '\n':
        while len(stack) != 0:
            res.append(stack.pop())

print(''.join(res))

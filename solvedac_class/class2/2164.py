from collections import deque

queue = deque()
n = int(input())

for i in range(n):
    queue.append(i + 1)

while(len(queue) > 1):
    queue.popleft()
    k = queue[0]
    queue.popleft()
    queue.append(k)
    '''
    위의 코드를 아래 코드처럼 변경 가능
    queue.popleft()
    queue.append(queue.popleft())

    '''

print(queue[0])

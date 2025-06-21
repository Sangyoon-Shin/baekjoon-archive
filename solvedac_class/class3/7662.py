import sys
import heapq
input = sys.stdin.readline

t = int(input())

for i in range(t):
    k = int(input())
    for j in range(t):
        minheap = []
        maxheap = []
        command, value = map(str, input().split())
        intvalue = int(value)
        if command == 'I':
            # ...
            heapq.heappush(minheap, intvalue)
            if j == 0:
                maximum = intvalue
                minimum = intvalue
            else:
                if intvalue >= maximum:
                    maximum = intvalue
                if intvalue <= min:
                    min = intvalue

        elif command == 'D' and value == '1':
            # ...
            arr.

        elif command == 'D' and value == '-1':
            # ...


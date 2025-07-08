# 값이 우선순위
# 오름차순, 내림차순으로 정렬된 우선순위 큐 두개 만들고
# 각각 최대깂, 최소값을 삭제한느 명령어인지에 따라 각 우선순위 큐에서 제거
# 값 삽입할 때, 양쪽 힙큐에 다 넣고, hashtable에도 넣어주기
# hashtable 만들어야 함. 동일한 정수 들어올 수 있기 때문에 개수 세줘야 할 듯
# 값 삭제할 때, hashtable에서 해당하는 값 삭제해주기
# del 딕셔너리[키]로 반대편 heap에서도 지워주면서 update해주면 어떨까..

import sys
import heapq
input = sys.stdin.readline

T = int(input())
for i in range(T):
    res = {}
    ascheap = [] # 오름차순 힙큐. 기본이 오름차순 정렬. 뽑으면 최솟값
    descheap = [] # 내림차순 힙큐. 뽑으면 최댓값
    k = int(input())
    for j in range(k):
        command, n = map(str, input().strip().split())
        n = int(n)
        if command == 'I':
            if n not in res.keys():
                res[n] = 1
            else:
                res[n] += 1
            heapq.heappush(ascheap, n)
            heapq.heappush(descheap, -n)
        elif command == 'D' and n == 1: # n == 1일때 최댓값 뽑기
            while True:
                if len(descheap) == 0:
                    break
                else:
                    value = -heapq.heappop(descheap)
                    if res[value] == 0:
                        continue
                    else:
                        res[value] -= 1
                        break
            
        elif command == 'D' and n == -1: # n == -1일때 최솟값 뽑기
            while True:
                if len(ascheap) == 0:
                    break
                else:
                    value = heapq.heappop(ascheap)
                    if res[value] == 0:
                        continue
                    else:
                        res[value] -= 1
                        break

    while len(descheap) > 0 and (-descheap[0] not in res.keys() or res[-descheap[0]] == 0):
        -heapq.heappop(descheap)
    while len(ascheap) > 0 and (ascheap[0] not in res.keys() or res[ascheap[0]] == 0):
        heapq.heappop(ascheap)
    
    if len(descheap) == 0 or len(ascheap) == 0:
        print("EMPTY")
    else:
        print(-descheap[0], ascheap[0])


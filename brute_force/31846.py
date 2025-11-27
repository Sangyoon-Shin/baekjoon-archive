import sys
input = sys.stdin.readline

n = int(input())
word = input().rstrip()
q = int(input())

for i in range(q):
    l, r = map(int, input().split())
    qq = word[l - 1:r]
    maximum = 0
    for j in range(len(qq)):
        cnt = 0
        front = qq[:j]
        rear = qq[j:]
        count = min(len(front), len(rear))
        front = list(reversed(front))
        for k in range(count):
            if front[k] == rear[k]:
                cnt += 1
        if cnt > maximum:
            maximum = cnt
    print(maximum)
        


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().strip().split()))
seq.sort()

s = []
used = [False] * n

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(n):
        if used[i]:
            continue
        else:
            used[i] = True
            s.append(seq[i])
            dfs()
            s.pop()
            used[i] = False

dfs()

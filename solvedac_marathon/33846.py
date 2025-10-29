import sys
input = sys.stdin.readline

n, t = map(int, input().split())

arr = list(map(int, input().split()))
sortedarr = sorted(arr[:t]) + arr[t:]
print(*sortedarr)
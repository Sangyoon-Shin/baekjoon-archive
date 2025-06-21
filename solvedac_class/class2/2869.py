import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())

end = v - b
cnt = end // (a - b)
rest = end % (a - b)

if rest == 0:
    print(cnt)
else:
    print(cnt + 1)
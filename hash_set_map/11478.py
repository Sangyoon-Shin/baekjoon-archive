import sys
input = sys.stdin.readline

# 입력 제한 1000. O(n^2)으로 짜도 됨

string = input().strip()
res = set()

for i in range(len(string)):
    for j in range(i, len(string)):
        res.add(string[i:j + 1])

print(len(res))



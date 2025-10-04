import sys
input = sys.stdin.readline

n = int(input())
lens = int(input())
s = input().strip()

# O는 n개, I는 n + 1개. 총 2n + 1개 저장해야함
p = ['' for i in range(2*n + 1)]

for i in range(2*n + 1):
    if i % 2 == 0:
        p[i] = 'I'
    else:
        p[i] = 'O'

p_str = ''.join(p)
print(s.count(p_str))




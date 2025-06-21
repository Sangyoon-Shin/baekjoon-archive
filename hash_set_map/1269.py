import sys
input = sys.stdin.readline

# n, m = map(int, input().split())
# aarr = set()
# barr = set()
# ans = set()

# avalues = list(map(int, input().split()))
# bvalues = list(map(int, input().split()))

# for i in range(len(avalues)):
#     aarr.add(avalues[i])

# for j in range(len(bvalues)):
#     barr.add(bvalues[j])

# for i in barr:
#     if i not in aarr:
#         ans.add(i)

# for j in aarr:
#     if j not in barr:
#         ans.add(j)

# print(len(ans))

n, m = map(int, input().split())
aset = set(map(int, input().split()))
bset = set(map(int, input().split()))

ans = (aset - bset) | (bset - aset)
print(len(ans))
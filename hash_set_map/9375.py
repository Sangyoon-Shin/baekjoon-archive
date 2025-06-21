import sys
input = sys.stdin.readline
from itertools import combinations

# 카테고리 하나일땐 nC1
# 카테고리 여러 개 일 때 -> 옷 개수 + nC1. 

t = int(input())

cat = set()
clo = set()
for i in range(t):
    n = int(input())
    for j in range(n):
        clothes, category = map(str, input().strip().split())
        clo.add(clothes)
        if category not in cat:
            cat.add(category)
        else:
            pass
    if len(cat) == 1:
        print(len(clo))
    else:
        comb = []
        # cat = list(cat) # 여기서 이렇게 바꿔버리면 2번째 테스트 케이스에서 cat이 list로 바뀜. 반드시 새로운 배열 만들어주기
        listcat = list(cat)
        for k in combinations(listcat, 1):
            comb.append(k)
        print(len(clo) + len(comb))
    # 다음 테스트 케이스 전에 비워줘야함
    cat.clear()
    clo.clear()
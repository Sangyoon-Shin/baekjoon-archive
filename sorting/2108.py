import sys
input = sys.stdin.readline

def myround(n):
    if n >= 0:
        if n - int(n) >= 0.5:
            return int(n) + 1
        else:
            return int(n)
    else:
        if n - int(n) <= -0.5:
            return int(n) - 1
        else:
            return int(n)

    
value = []
most = {}
mostlist = []
n = int(input())

for i in range(n):
    k = int(input())
    value.append(k)
    if k in most:
        most[k] += 1
    else:
        most[k] = 1

value.sort()

avg = myround(sum(value) / n)
print(avg)

mid = value[int(n/2)]
print(mid)

# map으로 저장해놓은 애들 다시 리스트로 반환하고 (키, 값) 쌍에서 1. 카운트 값 기준으로 내림차순 정렬   2. 출현 값 기준으로 오름차순 정렬
# 거기서 값[0], 값[1] 비교해서 같으면 값[1] 출력 다르면, 값[0] 출력하면 될 듯
for k, v in most.items(): 
    mostlist.append((k, v))

mostlist.sort(key=lambda x:(-x[1], x[0]))
if len(mostlist) == 1:
    val, cnt = mostlist[0]
    print(val)
else:
    firstval, firstcnt = mostlist[0]
    secondval, secondcnt = mostlist[1]
    if firstcnt != secondcnt:
        print(firstval)
    else:
        print(secondval)
        

gap = max(value) - min(value)
print(gap)




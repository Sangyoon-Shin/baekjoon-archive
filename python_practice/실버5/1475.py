import sys
input = sys.stdin.readline

n = list(map(int, list(input().strip())))
cnt = {}

for i in n:
    if i not in cnt:
        cnt[i] = 1
    else:
        cnt[i] += 1

max = 0
maxidx = -1
for i in cnt.keys():
    if cnt[i] > max:
        max = cnt[i]
        maxidx = i

# 6이나 9가 제일 많이 나온 값일 경우에만 바꿔보기 시도. 아닌 경우는 그냥 max 만큼의 세트 필요
# 6, 9 나오는 개수 더해서 그걸 2로 나누고 남은 나머지는 더해주기. 
# 그 값이 idx 6, 9 를 제외한 항목의 개수보다 큰지 작은지 비교하며 max 업데이트
if maxidx == 6 or maxidx == 9:
    if 6 in cnt and 9 in cnt:
        max = cnt[6] + cnt[9]
        if max % 2 == 1:
            max = (max // 2) + 1
        else:
            max = max // 2

    elif 6 not in cnt and 9 in cnt:
        if max % 2 == 1:
            max = cnt[9] // 2 + 1
        else:
            max = cnt[9] // 2

    elif 6 in cnt and 9 not in cnt:
        if max % 2 == 1:
            max = cnt[6] // 2 + 1
        else:
            max = cnt[6] // 2
        
    for i in cnt:
        if i != 6 and i != 9:
            if cnt[i] > max:
                max = cnt[i]
    print(max) 
else:
    print(max)

    

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

diff = []
for i in range(n):
    a, b = map(int, input().split())
    diff.append(b - a)

# 차이를 저장하고, 그 차이를 오름차순으로 정렬하면? 만약에 a가 b보다 크면 음수니까 앞순위가 됨.
# 그리고 k개 만큼 낙찰받아야 하니까 diff[k-1]이 정답이 됨
diff.sort() 
ans = diff[k -1]

if ans <= 0: # 차이가 같거나 음수면 a가 이미 낙찰을 한 상태니까 x를 증가시킬 필요가 없음
    print(0)
else:
    print(ans)






    
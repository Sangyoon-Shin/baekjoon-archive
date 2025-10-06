# itertools 에서 중복조합 가져와서 푼 버전
# from itertools import combinations_with_replacement
# n, m = map(int, input().split())

# num = []
# for i in range(n):
#     num.append(i + 1)

# for c in combinations_with_replacement(num, m): 
#     print(*c)


# dfs, 백트래킹 사용
n, m = map(int, input().split()) 
s = []
def dfs(start):
    if len(s) == m: # 탈출 조건은 s의 길이가 m이 되었을 때
        print(' '.join(map(str, s)))
        return
    for i in range(start, n + 1): # start부터 n까지 값을 증가시킴으로써 비내림차순 유지.
        s.append(i) # 값을 하나 넣고
        dfs(i) # 그 값을 넣은 상태에서 판단. 만약에 i를 넣었을 때 배열 길이가 m과 같아지면 그 때의 값을 출력하는거고, 아니면 start부터 추가
        s.pop() # 다시 뽑아서 선택 되돌리기 = 백트래킹
dfs(1)
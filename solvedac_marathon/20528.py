import sys
input = sys.stdin.readline

n = int(input())
words = list(input().strip().split())

# 팰린드롬 문자열이니까 앞, 뒤 글자가 같다
# 그러면 모든 단어의 시작과 끝이 같은 경우에만 끝말잇기가 가능하겠네
start = words[0][0]
flag = True
for i in words:
    if start != i[0]:
        print(0)
        flag = False
        break
    else:
        continue

if flag:
    print(1)
    

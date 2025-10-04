import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for i in range(n):
    words = input().strip()
    stack = []
    for word in words:
        if len(stack) == 0: # 비어있으면 일단 넣어야지
            stack.append(word)
        else: # 비어있지 않은 상태에서
            if word == 'A': # 넣는 값이 A. 바로 옆에 붙어있어야지만 뽑고 cnt 올릴 수 있음. ABBA 상태면 B는 뽑을거니까 스택에 A만 남아있을 것
                if stack[len(stack) - 1] == 'A': # python 문법적으로는 이제 listname[-1]을 써서 가장 마지막 idx 나타내자..
                    stack.pop()
                else:
                    stack.append(word)
            else: # B를 넣을 때
                if stack[len(stack) - 1] == 'B':
                    stack.pop()
                else:
                    stack.append(word)
    if len(stack) == 0: # 스택이 비어있으면 짝을 다 찾은거니까 좋은 단어
        cnt += 1

print(cnt)




            






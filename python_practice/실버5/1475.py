import sys
input = sys.stdin.readline

num = list(input().strip())

# 앞에서부터 스택에 쌓으면서 스택에 이미 있는 값이 나오면? 스택을 비워버리고 cnt++
# 9가 들어가는데 스택에 9가 있다면 6으로 바꿔서 넣자. 여기서 6도 있다면 스택 비워버리고 cnt++. 반대의 경우도 마찬가지
# 문제.. 연속된 숫자 들어왔을 때 순서를 바꾸면 더 작은 cnt 만들 수 있는 경우가 있음.

stack = []
cnt = 0
for i in num:
    if i not in stack:
        stack.append(i)

    elif i != '6' and i != '9' and i in stack:
        stack.clear()
        stack.append(i)
        cnt += 1
    
    elif i == '6' and '6' in stack:
        if '9' in stack:
            stack.clear()
            stack.append(i)
            cnt += 1
        else:
            stack.append('9')

    elif i == '9' and '9' in stack:
        if '6' in stack:
            stack.clear()
            stack.append(i)
            cnt += 1
        else:
            stack.append('6')

if len(stack) > 0:
    stack.clear
    cnt += 1
    print(cnt)
else:
    print(cnt)



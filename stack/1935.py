import sys
input = sys.stdin.readline

n = int(input())
ex = input().strip()
ex = list(ex)
value = {}
for i in range(n):
    num = int(input())
    value[chr(65 + i)] = num

# 연산자 나오기 전까지 숫자들 stack에 저장
# 연산자 나오면 stack에서 뽑은 두 수 끼리 연산 후 그 결과를 다시 stack에 넣기
# 위 과정 반복
stack = []
for i in ex:
    if i == '+':
        # 더하기
        first = stack.pop()
        second = stack.pop()
        new = first + second
        stack.append(float(new))
    elif i == '-':
        # 빼기
        first = stack.pop()
        second = stack.pop()
        new = second - first
        stack.append(float(new))
    elif i == '*':
        # 곱하기
        first = stack.pop()
        second = stack.pop()
        new = first * second
        stack.append(float(new))
    elif i == '/':
        # 나누기
        # 후위 표기식 앞에서 계산 CD/ 면 C/D로 해야함
        first = stack.pop()
        second = stack.pop()
        new = second / first
        stack.append(float(new))
    else:
        # 숫자는 stack에 push
        stack.append(float(value[i]))

res = stack.pop()
print(f"{res:.2f}")
import sys
input = sys.stdin.readline

n = int(input())
seq = [int(input()) for _ in range(n)]

st = []
res = []
cur = 1  

for x in seq:
    # x가 스택의 top이 될 때 까지 push 해줌.
    while cur <= x:
        st.append(cur)
        res.append('+')
        cur += 1

    if len(st) != 0 and st[-1] == x: # stack의 top이 원하는 값이 아니면 뽑을 수가 없음.
        st.pop()
        res.append('-')
    else:
        print("NO")
        sys.exit(0)

for i in res:
    print(i)

'''
# 처음에 짠 코드는 want in st 부분 때문에 O(n^2)
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
st = []

res = deque([int(input()) for i in range(n)])
result = []

cur = 1
want = res.popleft()
flag = False

while len(res) != 0:
    if want != cur: # 원하는 값이 넣어야 할 차례의 값인지 아닌지부터 비교
        if want in st: # 원하는 값이 넣어야 할 차례의 값은 아닌데, stack에 이미 있다면? 걔가 스택의 top이지 않은 이상 뽑을 수가 없음.
            if want == st[len(st) - 1]: # stack의 탑이 원하는 값이면 stack에서 뽑고 원하는 값 업데이트.
                st.pop()
                result.append("-")
                want = res.popleft()
            else: # stack의 탑이 원하는 값이 아니면 실패.
                flag = True
                print("NO")
                break
        else: # 원하는 값이 stack에 없으면 추가하고 다음 넣어야 할 값으로 cur++
            st.append(cur)
            result.append("+")
            cur += 1
    else: # 원하는 값이 넣어야 할 차례의 값이면 넣었다가 빼주면 됨.
        st.append(cur)
        result.append("+")
        cur += 1
        st.pop()
        result.append("-")
        want = res.popleft()

if flag:
    pass
else:
    result.append("-")
    for i in result:
        print(i)
'''
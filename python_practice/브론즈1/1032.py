import sys
input = sys.stdin.readline

arr = []
answer = []
n = int(input())

for i in range(n):
    string = list(input().strip())
    arr.append(string)

if n == 1:
    for i in range(len(arr[0])):
        print(arr[0][i], end='')
else:
    for i in range(len(arr[0])):
        flag = 0
        for j in range(n - 1):
            prev = arr[j][i]
            if prev == arr[j + 1][i]:
                continue
            else:
                answer.append('?')
                flag = 1
                break
        if flag == 0:
            answer.append(prev)

    for i in answer:
        print(i, end='')
        
                    
            
        
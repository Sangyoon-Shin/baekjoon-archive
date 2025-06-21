import sys
input = sys.stdin.readline

string = list(input().strip())

cnt = 0
for i in range(len(string)//10):
    for j in range(10):
        print(string[i * 10 + j], end ='')
    cnt += 1
    print(end='\n')

start = (len(string) // 10) * 10
for k in range(start, len(string)):
    print(string[k], end ='')
    
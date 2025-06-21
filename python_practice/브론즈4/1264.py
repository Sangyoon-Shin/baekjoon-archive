import sys

lists = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

while(1):
    a = sys.stdin.readline().strip()
    if(a == "#"): # '#'은 내부적으로 '#\n'인 상태. 즉 # != #\n임. readline 뒤에 srtip로 앞뒤 개행문자 없애거나 비교하는 값을 #\n으로 해야함.
        break
    else:
        cnt = 0
        for i in a:
            for j in lists:
                if(i == j):
                    cnt = cnt + 1
            
        print(cnt)

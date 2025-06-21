import sys
input = sys.stdin.readline

n, m = map(int, input().split())

word = {}
wordlist = []
ans = []

for i in range(n):
    string = input().strip()
    if len(string) >= m:
        if string in word:
                word[string] += 1
            
        else:
            word[string] = 1
    else:
         pass
    
for key, value in word.items():
     wordlist.append((key, value))

# print(wordlist)

wordlist.sort(key=lambda wordlist:(-wordlist[1],-(len(wordlist[0])), wordlist[0]))
# 여러 조건으로 정렬할 때 key=lamda 사용
# 기본은 오름차순 정렬, 내림차순으로 정렬하고 싶을땐 - 붙여주기
# print(wordlist)

for x, y in wordlist:
     print(x)


    
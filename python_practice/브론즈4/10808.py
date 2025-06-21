import sys

list = [0 for i in range(26)]

word = sys.stdin.readline().strip()
for char in word:
    list[ord(char) - ord('a')] += 1 # ord: 문자에 대한 아스키값 반환   

print(*list)
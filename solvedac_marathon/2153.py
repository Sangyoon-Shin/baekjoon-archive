import sys
import math
input = sys.stdin.readline

string = list(input().strip())

numdict = {}

for i in range(26):
    numdict[chr((97 + i))] = i + 1

for i in range(26):
    numdict[chr((65 + i))] = 27 + i

sum = 0
for i in string:
    sum += numdict[i]

flag = 0 
for i in range(2, int(math.sqrt(sum)) + 1):
    if sum % i == 0:
        flag = 1
        break

if flag == 0:
    print("It is not a prime word.")
else:
    print("It is a prime word.")
        



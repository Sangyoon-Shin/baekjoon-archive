import sys

sentence = sys.stdin.readline() 

swap = sentence.swapcase()
# swapcase: 대문자는 소문자로, 소문자는 대문자로
# upper: 대문자를 소문자로
# lower: 소문자를 대문자로

print(swap)
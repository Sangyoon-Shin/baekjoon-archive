import sys
import math
input = sys.stdin.readline

string = input().rstrip()
n, m = map(int, string.split(':'))
num = math.gcd(n, m)
tostringn, tostringm = str(n//num), str(m//num)
print(tostringn + ':' + tostringm)
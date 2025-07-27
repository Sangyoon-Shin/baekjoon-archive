import sys
input = sys.stdin.readline

string = input().strip()

# replace 문법 -> string.replace(old, new, count) 
# count 안쓰면 해당하는 모든 old 부분 문자열에 대해 new로 치환
# count 쓰면 그 횟수 만큼 앞에서 부터 교체
# 주의할 점은 반환값이 바꾸고 난 후의 문자열임.
# "AAA"가 있고 ("AA", "BB")를 해주면 BBB가 되는게 아님. 맨 앞에부터 먼저 존재하는 AA를 바꿔서 BBA를 만들어주고 이후 문자열에 AA는 없으므로 BBA로 종료
string = string.replace('XXXX', 'AAAA')
string = string.replace('XX', 'BB')

if 'X' in string:
    print(-1)
else:
    print(string)

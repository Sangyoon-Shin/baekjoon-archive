import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = list(input().rstrip())
    cnt = 0
    while True:
        if ''.join(n) == '6174':
            print(cnt)
            break
        else:
            cnt += 1
            maxn = int(''.join(sorted(n, reverse=True)))
            minn = int(''.join(sorted(n)))
            n = str(maxn - minn).zfill(4)
            # zfill을 안써버리면 0999의 경우에서 0이 없는 상태로 str이 만들어져, max도 999, min도 999가 되어 무한루프 발생한다..
            # zfill(width)은 문자열 왼쪽에 0을 붙여서 width의 길이가 되는 문자열이 되도록 해준다..



            
            

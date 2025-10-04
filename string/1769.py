n = list(input().strip())
cnt = 0

if len(n) == 1:
    if int(n[0]) % 3 == 0:
        print(cnt)
        print("YES")
    else:
        print(cnt)
        print("NO")
else:
    while True:
        cnt += 1
        n = list(map(int, n))
        if sum(n) < 10:
            if sum(n) % 3 == 0:
                print(cnt)
                print("YES")
            else:
                print(cnt)
                print("NO")
            break
        else:
            n = list(str(sum(n))) # 여기서 문자열로 바꿔줘야 하네






import sys
input = sys.stdin.readline

def solution(n):
    arr = []
    for i in range(1, n + 1):
        if n % i == 0:
            if i == n:
                continue
            else:
                arr.append(i)

    sarr = list(map(str, arr))
    if sum(arr) == n:
        print(f"{n} =",' + '.join(sarr))
    else:
        print(f"{n} is NOT perfect.")
    

while True:
    n = int(input())
    if n == -1:
        break
    else:
        solution(n)



import sys
input = sys.stdin.readline

arr = []
stringidx = []

for i in range(3):
    arr.append(input().strip())

for idx in range(3):
    if arr[idx] == 'Fizz' or arr[idx] == 'Buzz' or arr[idx] == 'FizzBuzz':
        stringidx.append(idx)

# isdigit() 이라는 숫자 판별 함수 있음.
if 0 not in stringidx:
    arr.append(int(arr[0]) + 3)
elif 1 not in stringidx:
    arr.append(int(arr[1]) + 2)
elif 2 not in stringidx:
    arr.append(int(arr[2]) + 1)

if arr[3] % 3 == 0 and arr[3] % 5 == 0:
    print('FizzBuzz')
elif arr[3] % 3 == 0 and arr[3] % 5 != 0:
    print('Fizz')
elif arr[3] % 3 != 0 and arr[3] % 5 == 0:
    print('Buzz')
else:
    print(arr[3]) 

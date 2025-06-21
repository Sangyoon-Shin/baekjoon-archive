import sys

while(1):
    name, age, weight = map(str, sys.stdin.readline().split())
    if(name == '#' and age == '0' and weight.strip() == '0'):
        break
    if(int(age) > 17 or int(weight) >= 80):
        print(name + ' Senior')
    else:
        print(name + ' Junior')
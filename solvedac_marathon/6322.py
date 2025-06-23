import sys
import math
input = sys.stdin.readline

t = 1
while True:
    a, b, c = map(float, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    if c == -1:
        # a^2 + b^2 = c^2
        c = math.sqrt(a**2 + b**2)
        print(f"Triangle #{t}")
        print(f"c = {c:.3f}")

    elif a == -1:
        # a^2 = c^2 - b^2
        val = c**2 - b**2
        if val <= 0:
            print(f"Triangle #{t}")
            print("Impossible.")
            print()
        else:
            a = math.sqrt(val)
            print(f"Triangle #{t}")
            print(f"a = {a:.3f}")
            print()

    elif b == -1:
        # b^2 = c^2 - a^2
        val = c**2 - a**2
        if val <= 0:
            print(f"Triangle #{t}")
            print("Impossible.")
            print()
        else:
            b = math.sqrt(val)
            print(f"Triangle #{t}")
            print(f"b = {b:.3f}")
            print()
    t += 1



            

    


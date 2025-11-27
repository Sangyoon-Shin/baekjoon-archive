import sys
input = sys.stdin.readline

card = input().rstrip()

idx = 0
cardinfo = [set() for i in range(4)]
cardshape = {"P" : 0, "K" : 1, "H" : 2, "T" : 3}
while True:
    if idx >= len(card):
        break
    else:
        shape = card[idx] 
        x, y = card[idx + 1], card[idx + 2]
        num = x + y
        idx += 3

        if shape in cardshape:
            if num in cardinfo[cardshape[shape]]:
                print("GRESKA")
                sys.exit(0)
            else:
                cardinfo[cardshape[shape]].add(num)

for i in range(4):
    print(13 - len(cardinfo[i]), end=' ')



            
        


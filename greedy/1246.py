import sys
input = sys.stdin.readline

n, m = map(int, input().split())
price = [int(input()) for _ in range(m)]

price.sort() 

max_profit = 0
best_price = 0

for i in range(m):
    candidate = price[i]               
    buyers = m - i                     
    eggs_sold = min(n, buyers)         
    profit = candidate * eggs_sold

    if profit > max_profit:
        max_profit = profit
        best_price = candidate

print(best_price, max_profit)

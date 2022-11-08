import sys
input = sys.stdin.readline

n, m = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)], reverse=True)

def using(coin, money, cnt):
    if coin > money:
        return cnt, money
    cnt += money // coin
    money = money % coin
    return cnt, money
cnt = 0
for coin in coins:
    cnt, m = using(coin, m, cnt)

print(cnt)





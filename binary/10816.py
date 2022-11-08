import sys, collections

input = sys.stdin.readline

n = int(input())
cards = sorted(list(map(int, input().split())))

m = int(input())
arrs = list(map(int, input().split()))

count = collections.Counter(cards)
res = []
for arr in arrs:
    if arr in count:
        res.append(count[arr])
    else:
        res.append(0)

for r in res:
    print(r, end= ' ')




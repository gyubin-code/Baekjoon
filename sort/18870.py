import sys
import collections
lambda input: sys.stdin.readline().rstrip
n = int(input())
arr = list(map(int, input().split(" ")))
tmp = list(sorted(set(arr)))
temp = collections.defaultdict(int)

for i in range(len(tmp)):
    temp[tmp[i]] = i
res = []
for i in arr:
    res.append(temp[i])

for i in res:
    print(i, end=' ')


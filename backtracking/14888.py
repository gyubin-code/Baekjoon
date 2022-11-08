import itertools
import sys, collections
lambda input: sys.stdin.readline().rstrip
#
# 2
# 5 6
# 0 0 1 0
n = int(input())
arr = list(map(int, input().split(' ')))
operator = list(map(int, input().split(' ')))
op = []
for i, v in enumerate(operator):
    for j in range(v):
        op.append(i)

res_max = -1e9
res_min = 1e9

for i in itertools.permutations(op):
    res = arr[0]
    for j in range(1, len(arr)):
        if i[j-1] == 0:
            res += arr[j]
        elif i[j-1] == 1:
            res -= arr[j]
        elif i[j-1] == 2:
            res *= arr[j]
        elif i[j-1] == 3:
            if res > 0:
                res //= arr[j]
            else:
                res = -(abs(res) // arr[j])

    res_max = max(res_max, res)
    res_min = min(res_min, res)

print(res_max)
print(res_min)


import sys, itertools
input = sys.stdin.readline

n = int(input())
flag = 0
res = 1e9

products = list(itertools.product('123', repeat=n))

# input
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def check(args):
    for i, v in enumerate(args):
        if i == 0:
            continue
        else:
            if args[i-1] == v:
                return False

    return True

for p in products:
    if check(p):
        tmp = 0

        ps = list(map(int, p))

        for i, v in enumerate(ps):
            tmp += arr[i][v-1]

        res = min(res, tmp)

print(res)





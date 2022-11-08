import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

res = []
tmp = [n-_ for _ in range(n)]
q = []
flag = 0
q = []
answer = 0
while tmp or q:
    if q and q[-1] == arr[flag]:
        flag += 1
        res.append('-')
        q.pop()
    else:
        if tmp:
            x = tmp.pop()
            q.append(x)
            res.append('+')
        else:
            answer = 1
            break

if answer == 0:
    for i in res:
        print(i)
else:
    print('NO')








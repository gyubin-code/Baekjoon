import sys
input = sys.stdin.readline

n = int(input())
q = []
arr = []
for _ in range(n):
    arr.append(int(input()))

for i in arr:
    if i == 0:
        q.pop()
    else:
        q.append(i)

print(sum(q))
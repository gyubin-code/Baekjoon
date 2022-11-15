import sys

input = sys.stdin.readline

n = int(input())

N = 45

tn = [1]
for i in range(2, N):
    tn.append(tn[-1] + i)
def solve(n):
    for i in range(N-1):
        for j in range(i, N-1):
            for k in range(j, N-1):
                if tn[i] + tn[j] + tn[k] == n:
                    return 1

    return 0


for i in range(n):
    k = int(input())
    print(solve(k))


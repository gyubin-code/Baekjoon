import sys
input = sys.stdin.readline

n = int(input())
times = []

for _ in range(n):
    a, b = map(int, input().split())
    times.append((a, b))


times =sorted(times, key=lambda x: (x[1], x[0]))

cur = 0
answer = 0
print(times)

for i in range(n):
    if cur <= times[i][0]:
        cur = times[i][1]
        answer += 1

print(answer)

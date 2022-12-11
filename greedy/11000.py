import sys, heapq
input = sys.stdin.readline

n = int(input())
times = []

for _ in range(n):
    a, b = map(int, input().split())
    times.append((a, b))

times = sorted(times)

q = [0] # 수업 진행중
for a, b in times:
    if q[0] <= a: # 가장 빨리 끝나는 시간 <= 시작하는 시간 -> 최적화 작업
        heapq.heappop(q)
    heapq.heappush(q, b)

print(len(q))
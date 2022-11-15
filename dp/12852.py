import sys, collections
input = sys.stdin.readline

n = int(input())

dp = [1e9] * (n+1)
q = collections.deque()
q.append(n)
answer_q = []
answer_cnt = 1e9

def solve(n, cnt):
    # dfs 사용
    global answer_cnt, answer_q
    if n == 1:
        cnt += 1

        if answer_cnt > cnt:
            answer_cnt = cnt
            answer_q = q.copy()

        return
    for i in (n%3, n%2, n-1):
        if i == n%3:
            if i == 0:
                q.append(n//3)
                solve(n//3, cnt+1)
                q.pop()
        elif i == n%2:
            if i == 0:
                q.append(n//2)
                solve(n//2, cnt+1)
                q.pop()
        elif i == n-1:
            q.append(n-1)
            solve(n-1, cnt+1)
            q.pop()


solve(n, 0)
print(answer_cnt)
print(*answer_q)
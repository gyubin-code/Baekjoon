import sys
input = sys.stdin.readline
def solve(l, p, v):
    section = v // p

    answer = section * l

    if v % p > l:
        answer += l
    else:
        answer += v%p

    return answer

cnt = 1
while 1:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    print(f"Case {cnt}: {solve(l, p, v)}")
    cnt += 1

import sys

lambda input: sys.stdin.readline().rstrip

def solve(n: int, pi: list):
    pi = sorted(pi)
    result = 0
    for i in range(len(pi), 0, -1):
        result += i*pi[len(pi)-i]
    print(result)


if __name__ =='__main__':

    n = int(input())

    pi = list(map(int, input().split()))

    solve(n, pi)


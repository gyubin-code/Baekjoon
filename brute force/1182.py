import itertools
import sys
input = sys.stdin.readline
n, S = map(int, input().split())

nums = list(map(int, input().split()))

def find():
    answer = 0
    for i in range(1, n+1):
        c = itertools.combinations(nums, i)
        for case in c:
            if sum(case) == S:
                answer += 1
    return answer


print(find())



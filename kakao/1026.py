import sys

input = sys.stdin.readline

#  a의 가장 작은수와 를 곱한다.

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

answer = 0
for i in range(n):
    answer += a[i] * b[i]

print(answer)
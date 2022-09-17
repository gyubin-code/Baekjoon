import sys

input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort()

# 모든 로프를 이용하여 가장 적은 무게로 드는 방법
# 가장 적은로프를 뺴고, 나머지 개수로 드는 방법,,
# 최대 중량 구하기
answer = 0
for i in range(n):
    temp = (n-i) * arr[i]
    # if 기존 answer 보다 계산해본것이 더 크다면?
    if answer <= temp:
        answer = temp

print(answer)

import sys
input = sys.stdin.readline

n = int(input())

arr = sorted(list(map(int, input().split())))

res = int(input())

i = 0
j = len(arr)-1

answer = 0

while 1:
    if i >= j:
        break

    tmp = arr[i] + arr[j]

    if tmp == res:
        i += 1
        j -= 1

        answer += 1
    elif tmp > res:
        j -= 1
    else:
        i += 1

print(answer)


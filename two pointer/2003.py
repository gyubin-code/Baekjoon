import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))
array = [0]
for i, a in enumerate(arr):
    array.append(array[i] + a)
i = 0
j = 1
answer = 0

while 1:
    if j > len(arr):
        break
    tmp = array[j] - array[i]
    if tmp == m:
        answer += 1
        i += 1
        j += 1
    elif tmp > m:
        i += 1
    else:
        j += 1

print(answer)





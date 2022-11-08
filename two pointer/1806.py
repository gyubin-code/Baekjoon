import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
array = [0]
for i,a in enumerate(arr):
    array.append(array[i] + a)

i = 0
j = 1
answer = 1e9

while 1:
    if i >= j or j > len(arr):
        break
    tmp = array[j] - array[i]
    if tmp >= s:
        answer = min(answer, j - i)
        i += 1
    elif tmp < s:
        j += 1

if answer == 1e9:
    answer = 0
print(answer)
import sys, math

input = sys.stdin.readline

n = int(input())

def is_prime_number(n):
    array = [True for i in range(n+1)]

    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [i for i in range(2, n+1) if array[i]]

arr = is_prime_number(n)

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
    if tmp == n:
        answer += 1
        i += 1
        j += 1
    elif tmp > n:
        i += 1
    else:
        j += 1


print(answer)
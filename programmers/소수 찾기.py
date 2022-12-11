import itertools
import math
def is_prime_number(n):
    array = [True for i in range(n+1)]

    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    return [i for i in range(2, n+1) if array[i]]

def solution(numbers):
    answer = 0
    numbers = [n for n in numbers]
    ans = []
    len_n = range(1, len(numbers)+1)

    # 모든 숫자 만들기
    for i in len_n:
        for comb in itertools.permutations(numbers, i):
            # print(comb)
            tmp = ''
            for c in comb:
                tmp += c
            ans.append(int(tmp))

    ans = set(ans)

    max_ans = max(ans)

    array = is_prime_number(max_ans)

    for i in ans:
        if i in array:
            answer += 1

    # print(answer)
    # print(ans)
    return answer
solution('17')

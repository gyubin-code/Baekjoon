import collections


def number(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]

def is_prime(k):
    if k == 2 or k == 3: return True
    if k % 2 == 0 or k < 2: return False

    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True
def solution(n, k):
    answer = 0
    n = number(n, k)
    n_list = n.split('0')

    for n in n_list:
        if n == "":
            continue
        if is_prime(int(n)):  # n이 소수인 경우 answer+=1
            answer += 1

    print(answer)
    return answer


solution(10, 2)
solution(437674, 3)
solution(110011, 10)
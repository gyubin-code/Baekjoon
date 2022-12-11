import itertools

def check(a, b):
    # 3000001 3 -> 3, 30000001
    return

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    answer = str(int(''.join(numbers)))
    return answer

# print(solution([6, 10, 2]))
print(solution([3, 3000001, 34, 5, 9]))
def get_divisor(n):
    array = []
    for i in range(1, n+1):
        if n % i == 0:
            array.append([i, n//i])
    return array

def calculate_brown(a, b, y):
    return 1 if 2*a + 2*b + 4 == y else 0

def solution(brown, yellow):
    answer = []

    array = get_divisor(yellow)

    for a in array:
        x, y = a
        if x >= y and [x, y] not in answer:
            if calculate_brown(x, y , brown):
                answer.append(x+2)
                answer.append(y+2)
                break


    # print(answer)
    return answer

solution(10, 2)
solution(8, 1)

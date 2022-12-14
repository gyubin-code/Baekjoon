import math


def solution(x, y, d):
    # write your code in Python 3.8.10
    if x == y:
        return 0
    cnt = math.ceil(y-x/d)
    return cnt

solution(10, 85, 30)
from collections import Counter
from functools import reduce

def solution(clothes):
    counter = Counter([type for clothe, type in clothes])
    answer = reduce(lambda acc, cur: acc*(cur+1), counter.values(), 1) - 1
    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
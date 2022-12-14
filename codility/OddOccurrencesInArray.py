# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections


def solution(arr):
    # write your code in Python 3.8.10
    a = collections.Counter(arr)
    for i, v in a.items():
        if v % 2 == 1:
            return i
    return

solution([9,3,9,3,9,7,9])
solution([1,1,1,2,3,2,3])
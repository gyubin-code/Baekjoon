import itertools


def solution(word):
    answer = 0
    # words = ['a', 'e', 'i', 'o', 'u']
    a = 'AEIOU'*5
    words = []
    for i in range(1, 6):
        for w in itertools.permutations(a, i):
            words.append(''.join(w))
    # print(sorted(set(words)))
    words = sorted(set(words))

    return words.index(word) + 1

    # return answer
solution("AAAAE")

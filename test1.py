import itertools


def prefix(s, dic):
    d = []
    n = len(s)
    for di in dic:
        if di[:n] == s:
            d.append(di)
    return d


def postfix(s, dic):
    d = []
    n = len(s)
    for di in dic:
        if di[len(di) - n:len(di)] == s:
            d.append(di)
    return d


def lengthMath(s, dic):
    d = []
    n = len(s)  # 총길이
    must_n = 0
    flag = 0
    for i, v in enumerate(s):
        if i == 0 and v != '@':
            # 접두사
            flag = 1
        if v != '@':
            must_n += 1

    if flag == 1:
        # 접두사 ac@@
        for di in dic:
            if di[:must_n] == s[:must_n] and len(di) == n:
                d.append(di)
    else:
        # 접미사 @@ab
        for di in dic:
            if di[len(di) - must_n:len(di)] == s[len(s) - must_n:len(s)] and len(di) == n:
                d.append(di)
    return d


def setdic(dic):
    d = dic.copy()
    for i in range(len(dic)):
        for j in range(len(dic)):
            if i == j:
                continue
            tmp = dic[i] + dic[j]
            if tmp not in d:
                d.append(tmp)
    print(d)
    return d


def solution(dictionary, command):
    answer = []

    for i, c in enumerate(command):
        if i == 0:
            dictionary = setdic(dictionary)
        if c[0] == "prefix":
            dictionary = prefix(c[1], dictionary)
        elif c[0] == "postfix":
            dictionary = prefix(c[1], dictionary)
        elif c[0] == 'lengthMatch':
            dictionary = lengthMath(c[1], dictionary)
        print(dictionary)

    answer = dictionary
    return answer


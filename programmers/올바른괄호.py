def solution(s):
    answer = True
    q = []
    for i in s:
        if i == '(':
            q.append()
        else: q.pop()
    if q:
        answer = False
    return answer
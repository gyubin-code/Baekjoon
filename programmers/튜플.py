def solution(s):

    lst = []
    tmp = ''
    flag = 0
    for i in s[1: len(s)-1]:
        if i == '{':
            flag = 1
        elif i == '}':
            flag = 0
            lst.append(list(map(int,tmp.split(','))))
            tmp = ''
        elif flag == 1:
            tmp += i

    lst = sorted(lst, key = lambda x: len(x))
    cnt = 0
    answer = []
    answer += lst[0]
    for i in range(1, len(lst)):
        tmp = [x for x in lst[i] if x not in answer]
        answer += tmp

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
import collections


def solution(s):
    answer = []
    # 문자열중에 가장 긴것을 찾는것
    if len(s) == 1:
        return 1

    # 문자열을 n개 단위로 자를때까지

    for i in range(1, len(s) + 1):
        r = ''
        cnt = 1
        t = s[:i]
        print(t)
        for j in range(i , len(s) + i, i): # n개 단위로 나누기

            if t == s[j: j + i]:
                cnt += 1
            else: #
                if cnt != 1:
                    r = r + str(cnt) + t
                else: #
                    r = r + t

                t = s[j: j + i]
                cnt = 1
        answer.append(len(r))

    print(min(answer))


    return min(answer)


solution("aabbaccc")
solution("ababcdcdababcdcd")
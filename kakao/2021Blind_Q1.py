import collections


def solution(new_id):
    point = 0
    answer = ''
    q = collections.deque()

    for i in range(len(new_id)):
        # 소문자, 숫자, 빼기, 언더바, 대문자, 스페이스
        o = ord(new_id[i])
        if 97 <= o <= 122 or 48 <= o <= 57 or o == 45 or o == 95 or 65 <= o <= 90 or o == 0 or o == 46:
            # 대문자
            if 65 <= o <= 90:
                q.append(chr(o + 32))

            if 97 <= o <= 122 or 48 <= o <= 57 or o == 45 or o == 95 :
                q.append(new_id[i])
            # 스페이스
            if o == 0:
                q.append('a')

            # .인 경우
            if new_id[i] == '.':
                if point == 0:
                    point = 1
                    q.append(".")
            # .이 아니면 변경
            else:
                point = 0

    if q and q[0] == '.':
        q.popleft()

    if q and q[-1] == '.':
        q.pop()

    while len(q) >= 16:
        q.pop()

    if q and q[-1] == '.':
        q.pop()

    while len(q) <= 2:
        if q:
            q.append(q[len(q) - 1])
        else:
            q.append('a')

    for i in q:
        answer += i

    print(answer)
    return answer

# solution("...!@BaT#*..y.abcdefghijklm")
# solution("z-+.^.")
solution("=.=")
solution("123_.def")
solution("abcdefghijklmn.p")
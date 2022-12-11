import collections
def check(n, citations):
    cnt = 0
    for i in citations:
        if n <= i:
            cnt += 1

    return cnt

def solution(citations):
    answer = 0
    citations.sort()
    max_n = max(citations)
    # 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
    # 1234
    # 2 번 이상 인용된 논문 3개
    # 2번 이하 2개

    print(enumerate(citations))

    # print(citations)
    for i in range(max_n):
        x = check(i, citations)
        if i <= x:
            answer = max(answer, i)
    # print(answer)
    return answer

solution([3, 0, 6, 1, 5])
solution([6, 5, 5, 5, 3, 2, 1, 0])
# solution([1, 1, 1, 1])
# solution([1, 2, 3, 4])
# solution([0, 0])

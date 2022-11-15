import collections
def solution(commands, messageID):
    answer = []

    q = []
    answer_q_messageDs= []
    flag  = 0
    dic = collections.defaultdict(int)

    dic["MY"] = 0
    for c in commands:
        if c[0] == 'I':
            dic[c[1]] = 0

        if c[2] == messageID:
            flag = 1
        if flag == 1:
            dic[c[1]] = 1 # 읽었다는 표시
    cnt = 0
    for i, d in dic.items():
        print(d)
        if d == 0:
            cnt += 1

    print(dic)
    print(cnt)

    return cnt

members = ["A", "B"]
commands = [["W", "MY", "1"], ["W", "A", "7"], ["W", "B", "4"], ["W", "MY", "9"], ["W", "A", "11"], ["R", "B", ""]]
messageIDS = "11"
print(solution(commands, messageIDS))
members = ["A"]
commands = [["W", "MY", "1"],["W", "A", "3"]]
messageIDS = ["8"]
print(solution(commands, messageIDS))


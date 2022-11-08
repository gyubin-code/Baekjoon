import collections

cnt = 1
command_dic = dict()
def in_dic(s):
    # 없는 값이만 dic에 넣어주고 해당 숫자를 리턴
    # 있는 값이면 해당 값 찾아서 리턴
    global command_dic
    if s not in command_dic:
        global cnt
        cnt += 1
        command_dic[s] = cnt
    else:
        return command_dic[s]
    return cnt

def make_range(v, a, b, c, d, board):
    # v로 arr1 ~ arr2까지 변경

    for i in range(b, d+1):
        for j in range(a, c+1):
            board[j][i] = v

    return board

def find_range(m_list, v,c):
    # v, c 가 속해있는 n값을 가진 범위 찾기
    for i, m in enumerate(m_list):
        if m[0]<= v<= m[2] and m[1]<= c<= m[3]:

            return i, m

    return False

def reset(board, a, b, c, d):
    for i in range(a, c+1):
        for j in range(b, d+1):
            board[i][j] = 0

    return board

def solution(commands):
    answer = []


    d = collections.defaultdict(list)


    for command in commands:
        c = command.split()

        if c[0] == 'UPDATE':
            if len(c) == 3:
                d[c[1]].append([c[1], c[2]])
            else:
                d[c2].append(d[c[1]])
                del(d[c3])

        elif c[0] == 'MERGE':
            r = 0
            c1 = int(c[1])
            c2 = int(c[2])
            c3 = int(c[3])
            c4 = int(c[4])

            range_list = []

            for i in range(c1, c3+1):
                for j in range(c2, c4+1):
                    range_list.append([i, j])

            for k, values in d.items():
                for i, v in enumerate(values):
                    if v == (c1, c2):
                        del(d[k][i])
                        d[k].append(range_list)


        # elif c[0] == 'UNMERGE':


        # elif c[0] == 'PRINT':
        #     if board[int(c[1])][int(c[2])] == 0:
        #         answer.append('EMPTY')
        #     else:
        #         num = board[int(c[1])][int(c[2])]
        #
        #         for k, v in command_dic.items():
        #             if v == num:
        #                 answer.append(k)

    print(answer)
    return answer

commands =["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
solution(commands)

commands = ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
# solution(commands)
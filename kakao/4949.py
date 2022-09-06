import sys, collections

open_bracket = ['(', '[']
close_bracket = [')', ']']

def solve(input_line):
    q = collections.deque()
    flag = 0

    while True:
        node = input_line[flag]
        # 종료 조건
        if node == '.':
            break

        if node in open_bracket:
            q.append(node)

        elif node in close_bracket:
            if q:
                compare = q.pop()
                if node != ')' and compare == "(":
                    print('no')
                    return
                elif node != ']' and compare == "[":
                    print('no')
                    return
            # 큐가 빈경우
            else:
                print('no')
                return

        flag += 1

    if q:
        print('no')
        return
    elif flag == len(input_line)-1:
        print('yes')
        return


while True:
    input_line = sys.stdin.readline().rstrip()
    if input_line[0] == '.':
        break
    else:
        solve(input_line)
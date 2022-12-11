def solution(name):
    answer = 0
    names = [ord('A')] * len(name)
    names2 = [ord('A')] * len(name)

    for i, n in enumerate(name):
        names[i] = ord(n)
    for i, n in enumerate(name):
        names2[len(names)-1-i] = ord(n)
    a = ord('A')
    z = ord('Z') + 1
    answer1 = 0
    answer2 = 0

    for i, n in enumerate(names):
        if i == len(names)-1:
            answer1 += min(n - a, z - n)
            break
        elif n == a:
            answer1 += 1
            continue
        answer1 += min(n-a, z-n)
        answer1 += 1
    for i, n in enumerate(names2):
        if i == len(names)-1:
            answer2 += min(n - a, z - n)
            break
        elif n == a:
            answer2 += 1
            continue
        answer2 += min(n-a, z-n)
        answer2 += 1

    print(names, names2)
    print(answer1, answer2)

    return answer

# solution("JEROEN")
solution("JAN")
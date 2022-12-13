def search(word, target):
    answer = 0
    for i in range(len(word)):
        if word[i] != target[i]:
            answer += 1
    if answer == 1:
        return True
    return False
answer = 1e9


def solution(begin, target, words):
    global answer

    def dfs(w, words,  cnt):
        global answer

        if w == target:
            if answer > cnt:
                # print(words, cnt)
                answer = cnt
            return

        for i, v in enumerate(words):
            if search(w, v):
                dfs(v, words[:i]+words[i+1:], cnt+1)

    dfs(begin, words, 0)
    if answer == 1e9:
        answer = 0
    # print(answer)
    return answer

# solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
import collections
def solution(id_list, k):
    answer = 0
    id_dic = collections.defaultdict(int)
    for ids in id_list:
        id_l = set(ids.split()) # 최대 1장 없앰
        for i in id_l:
            if i in id_dic:
                id_dic[i] += 1
            else:
                id_dic[i] = 1
    for v in id_dic.values():
        if v > k:
            answer += k
        else:
            answer += v
    return answer

print(solution(["A B C D", "A D", "A B D", "B D"], 3))
print(solution(["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"], 3))
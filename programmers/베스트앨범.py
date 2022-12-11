import collections
def solution(genres, plays):
    answer = []
    counter = collections.defaultdict(int)
    for i in range(len(genres)):
        counter[genres[i]] += plays[i]
    counter = collections.Counter(counter).most_common()
    q = collections.defaultdict(list) # (500, i)
    for i in range(len(genres)):
        q[genres[i]].append([plays[i], i])
    for i in q.values():
        i.sort(key = lambda x: (x[0], -x[1]))

    for i in counter:

        if q[i[0]]:
            v, index = q[i[0]].pop()
            answer.append(index)
        if q[i[0]]:
            v, index = q[i[0]].pop()
            answer.append(index)



    return answer

solution(["classic", "pop", "classic", "classic", "pop"], 	[800, 600, 150, 800, 2500])
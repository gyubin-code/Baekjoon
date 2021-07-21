import sys
#k 나라보다 몇 나라가 위에있는지 ,, 알기위해 


n, k = map(int, input().split())
rank_table=[]
for _ in range(n):
    ranking = list(map(int, input().split()))
    if ranking[0] != k:
        rank_table.append(ranking)
    else:
        standard = ranking

count = 1
for i in range(len(rank_table)):
    if rank_table[i][1] > standard[1]: #k나라보다 금메달 많은경어
        count += 1

    elif rank_table[i][1] == standard[1]: #k나라보다 은메달이 많은경어
        if rank_table[i][2] > standard[2]:
            count += 1

        elif rank_table[i][2] == standard[2]: #동메달이 많은경우
            if rank_table[i][3] > standard[3]:
                count += 1
    
print(count)
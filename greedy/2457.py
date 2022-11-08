flowers = []
count = 0
n = int(input())

for _ in range(n):
    m1, d1, m2, d2 = map(int, input().split())
    flowers.append((m1*100+d1, m2*100+d2))

flowers.sort(key=lambda x:(x[0], x[1]))
start_date = 301
end_date = 0
while flowers:
    if start_date >= 1201 or start_date < flowers[0][0]:
        break

    for flower in flowers[:]:

        if start_date >= flower[0]:
            if end_date <= flower[1]:
                end_date = flower[1]
            flowers.remove(flower)
        else:
            break

    count += 1
    start_date = end_date

print(0 if start_date < 1201 else count)
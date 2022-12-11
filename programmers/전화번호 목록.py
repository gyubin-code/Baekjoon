def solution(phone_book):
    answer = True
    phone_book.sort()
    print(phone_book)

    ps = []  # 접두사
    for p in phone_book:
        if p not in ps:
            if ps:
                for i in ps:
                    if p.startswith(i):
                        answer = False
            ps.append(p)

        else:
            answer = False
            break

        if not answer:
            break

    return answer

solution(["119", "97674223", "1195524421"])
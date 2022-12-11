

def solution(low, high, img):
    answer = 0
    # 세로 위치를 정의
    x_img = []
    for i in range(len(img[0])):
        tmp = []
        for j in range(len(img)):
            tmp.append(img[j][i])
        x_img.append(tmp)



    for k in range(3, 51):
        # 3 * 3 부터 검사
        # 검사 범위는 전체
        # 0 부터
        # 길이가 4라면 4-3 을 포함하는 길이까지
        len_x = len(img[0])
        len_y = len(img)

        for j in range(len(img)): # y
            for i in range(len(img[0])): # x

                if i + k <= len_x and j + k <= len_y:

                    # 사각형이 가능하다면
                    if img[j][i:i+k].count('.') == 0 and img[j+k-1][i:i+k].count('.') == 0:
                        if x_img[i][j: j+k].count('.') == 0 and x_img[i+k-1][j:j+k].count('.') == 0:
                            shap = 0
                            # 내부 사각형 갯수 세기
                            for dy in range(j+1, j+k-1):
                                for dx in range(i+1, i+k-1):
                                    if img[dy][dx] == '#':
                                        shap += 1

                            if low<=(shap / pow((k-2), 2)) * 100<high:
                                answer += 1

       

    return answer

print(solution(25, 51, [".########......", ".####...#......", ".#.####.#.#####", ".#.#..#.#.#..##", ".#.##.#.#.#...#", ".#.####.#.#...#", ".#....###.#####", ".########......"]))
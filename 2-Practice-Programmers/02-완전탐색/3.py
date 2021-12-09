# [카펫] 카펫의 가로, 세로 크기 (완전탐색)

def solution(brown, yellow):
    # (완전탐색) yellow_h 모든 경우를 탐색
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            yellow_h = i
            yellow_w = yellow // i

            brown_cnt = (yellow_h + yellow_w) * 2 + 4
            if brown_cnt == brown:
                return [yellow_w + 2, yellow_h + 2]


print(solution(10, 2))  # [4, 3]
print(solution(8, 1))  # [3, 3]
print(solution(24, 24))  # [8, 6]

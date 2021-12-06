# [체육복] 수업을 들을 수 있는 학생의 최대값 (탐욕)

def solution(n, lost, reserve):
    result = set(range(1, n + 1))
    lost = set(lost)
    reserve = set(reserve)

    # 도난 제외
    result -= lost

    # 여분 있으면 포함
    result |= lost & reserve
    reserve -= lost & reserve

    # (탐욕) 대여 가능하면 포함
    for x in reserve:
        for e in [x - 1, x + 1]:
            if 1 <= e <= n and e not in result:
                result.add(e)
                break

    return len(result)


print(solution(5, [2, 4], [1, 3, 5]))  # 5
print(solution(5, [2, 4], [3]))  # 4
print(solution(3, [3], [1]))  # 2
print(solution(5, [2, 3, 4], [1, 2, 3]))  # 4 => 5번 반례

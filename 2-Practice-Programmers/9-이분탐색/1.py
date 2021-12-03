# [입국심사] 모든 사람이 심사를 받는 최소 시간 (이분탐색)

def solution(n, times):
    result = 0
    s = 0
    e = min(times) * n

    while s <= e:
        mid = (s + e) // 2

        # 심사받은 사람의 수
        count = sum([mid // x for x in times])

        if count >= n:
            result = mid
            e = mid - 1
        else:
            s = mid + 1

    return result


print(solution(6, [7, 10]))  # 28

# [징검다리] 바위 사이의 최소 거리 (이분탐색)

def get_count(target, a):
    n = len(a)
    count = 0
    i = 0
    j = 1

    while j < n:
        if a[j] - a[i] < target:
            count += 1
            j += 1
        else:
            i = j
            j = i + 1

    return count


def solution(distance, rocks, n):
    result = 0
    s = 0
    e = distance
    rocks.sort()

    while s <= e:
        mid = (s + e) // 2

        # 제거된 바위의 수
        count = get_count(mid, [0] + rocks + [distance])

        if count > n:
            e = mid - 1
        else:
            result = mid
            s = mid + 1

    return result


print(solution(25, [2, 14, 11, 21, 17], 2))  # 4

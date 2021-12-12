# [공유기 설치] 공유기 사이의 최대거리 (이분탐색)

import sys

n, c = map(int, input().split())
a = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

a.sort()


def get_count(a, dist):
    n = len(a)
    i = 0
    j = 1
    count = 1

    while j < n:
        if a[j] - a[i] >= dist:
            count += 1
            i = j
            j = i + 1
        else:
            j += 1

    return count


s = 1
e = a[-1] - a[0]
result = 0

while s <= e:
    mid = (s + e) // 2

    # count = get_count(a, mid)
    count = 1
    i = 0
    for j in range(1, n):
        if a[j] - a[i] >= mid:
            count += 1
            i = j

    if count >= c:
        result = mid
        s = mid + 1
    else:
        e = mid - 1

print(result)

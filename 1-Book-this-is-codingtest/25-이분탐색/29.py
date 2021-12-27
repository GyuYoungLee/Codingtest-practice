# [공유기 설치] 공유기 사이의 최대거리 (이분탐색)

import sys

n, c = map(int, input().split())
a = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

a.sort()

s = 1
e = a[-1] - a[0]
result = 0

while s <= e:
    mid = (s + e) // 2

    # 공유기 거리가 mid 일때 설치가능한 공유기 갯수
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

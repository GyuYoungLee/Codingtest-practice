# [치킨 배달] 도시의 치킨거리의 최소값 (구현, 완전탐색=조합)

import itertools

n, m = map(int, input().split())
house = []
chicken = []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            house.append((i, j))
        elif data[j] == 2:
            chicken.append((i, j))

result = int(1e9)  # 모든 케이스 중 최소값
for candidates in itertools.combinations(chicken, m):

    total = 0
    for hx, hy in house:
        dist = int(1e9)  # 가장 가까운 치킨집의 거리
        for cx, cy in candidates:
            dist = min(dist, abs(hx-cx) + abs(hy-cy))

        total += dist

    result = min(result, total)

print(result)

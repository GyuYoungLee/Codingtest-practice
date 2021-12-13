# [안테나] 거리의 합이 최소가 되는 안테나 설치 위치 (정렬)

import math

n = int(input())
house = list(map(int, input().split()))

house.sort()

print(house[(n - 1) // 2])

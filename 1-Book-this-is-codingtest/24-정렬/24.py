# [안테나] 안테나 위치 (정렬)

import math

n = int(input())
house = list(map(int, input().split()))

house.sort()

print(house[(n - 1) // 2])

# [안테나] 거리의 합이 최소가 되는 안테나 설치 위치 (정렬)

n = int(input())
house = list(map(int, input().split()))

house.sort()  # 정렬

i = (n - 1) // 2  # 가장 작은 값을 구해야 하므로
print(house[i])

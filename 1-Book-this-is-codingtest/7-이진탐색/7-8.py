# [떡볶이 떡 만들기] 절단기 높이의 최대값 (이진탐색)

N, M = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = max(data)

result = 0
while start <= end:
    mid = (start + end) // 2
    cutted = sum([x - mid for x in data if x > mid])

    if cutted >= M:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)

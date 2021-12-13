# [카드 정렬하기] 비교횟수의 최소값 (정렬)

import heapq
import sys

n = int(input())
qu = []
for _ in range(n):
    heapq.heappush(qu, int(sys.stdin.readline().rstrip()))

result = 0
while len(qu) >= 2:
    a = heapq.heappop(qu)
    b = heapq.heappop(qu)

    result += a + b
    heapq.heappush(qu, a + b)

print(result)

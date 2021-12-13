# [특정 수의 개수 구하기] (이분탐색)

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
nums = list(map(int, input().split()))

left = bisect_left(nums, x)
right = bisect_right(nums, x)

print(right - left if right - left > 0 else -1)

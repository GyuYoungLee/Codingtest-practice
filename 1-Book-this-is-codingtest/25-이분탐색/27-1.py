# [특정 수의 개수 구하기] (이분탐색)

import bisect

n, x = map(int, input().split())
nums = list(map(int, input().split()))

left = bisect.bisect_left(nums, x)
right = bisect.bisect_right(nums, x)

print(right - left if right - left > 0 else -1)

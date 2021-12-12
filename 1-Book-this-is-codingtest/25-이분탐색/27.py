# [특정 수의 개수 구하기] (이분탐색)

n, x = map(int, input().split())
nums = list(map(int, input().split()))

s = 0
e = n - 1

target = -1
while s <= e:
    mid = (s + e) // 2

    if nums[mid] > x:
        e = mid - 1
    elif nums[mid] < x:
        s = mid + 1
    else:
        target = mid
        break

if target == -1:
    print(-1)
else:
    count = 1

    i = target - 1
    while i >= 0 and nums[i] == x:
        count += 1
        i -= 1

    j = target + 1
    while j <= n - 1 and nums[j] == x:
        count += 1
        j += 1

    print(count)

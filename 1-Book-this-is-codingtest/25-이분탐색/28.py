# [고정점 찾기] (이분탐색)

n = int(input())
a = list(map(int, input().split()))

s = 0
e = n - 1

target = -1
while s <= e:
    mid = (s + e) // 2

    if a[mid] > mid:
        e = mid - 1
    elif a[mid] < mid:
        s = mid + 1
    else:
        target = mid
        break

if target == -1:
    print(-1)
else:
    print(a[target])

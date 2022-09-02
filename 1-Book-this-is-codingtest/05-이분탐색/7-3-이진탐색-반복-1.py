# [이진 탐색] 반복

def binary_search(a, x):
    start = 0
    end = len(a) - 1

    result = -1
    while start <= end:
        mid = (start + end) // 2

        if a[mid] <= x:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result


d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36))

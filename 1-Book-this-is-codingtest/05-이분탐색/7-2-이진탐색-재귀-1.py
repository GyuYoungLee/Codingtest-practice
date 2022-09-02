# [이진 탐색] 재귀

def binary_search(a, x, start, end):
    if start > end:
        return

    mid = (start + end) // 2

    global result
    if a[mid] <= x:
        result = mid
        binary_search(a, x, mid + 1, end)
    else:
        binary_search(a, x, start, mid - 1)

    return result


result = -1
d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36, 0, len(d) - 1))

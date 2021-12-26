# [이진 탐색] 재귀

def binary_search(a, x, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if a[mid] < x:
        return binary_search(a, x, mid + 1, end)
    elif a[mid] > x:
        return binary_search(a, x, start, mid - 1)
    else:
        return mid


d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36, 0, len(d) - 1))

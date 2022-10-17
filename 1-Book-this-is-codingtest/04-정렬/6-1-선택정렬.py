# [선택 정렬] 최소값을 찾아서 하나씩 넣는다

a = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
n = len(a)

for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
        if a[j] < a[min_idx]:
            min_idx = j

    a[i], a[min_idx] = a[min_idx], a[i]

print(a)

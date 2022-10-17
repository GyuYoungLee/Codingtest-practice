# [삽입 정렬] 하나씩 꺼내서 순서찾아 넣는다

a = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
n = len(a)

for i in range(1, n):
    for j in range(i, 0, -1):
        if a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
        else:
            break

print(a)

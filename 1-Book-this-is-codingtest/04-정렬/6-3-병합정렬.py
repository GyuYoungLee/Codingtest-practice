# [병합 정렬] 각자 정렬한 후 합친다

def merge_sort(a):
    if len(a) == 1:
        return a

    mid = len(a) // 2
    g1 = merge_sort(a[:mid])
    g2 = merge_sort(a[mid:])

    result = []
    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))

    if g1:
        result.extend(g1)
    else:
        result.extend(g2)

    return result


d = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(merge_sort(d))

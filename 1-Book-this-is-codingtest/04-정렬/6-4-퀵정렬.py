# [퀵 정렬] 나누고 갖자 정렬한다

def quick_sort(a):
    if len(a) <= 1:
        return a

    pivot = a[0]
    g1 = [x for x in a[1:] if x < pivot]
    g2 = [x for x in a[1:] if x >= pivot]

    return quick_sort(g1) + [pivot] + quick_sort(g2)


d = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(quick_sort(d))

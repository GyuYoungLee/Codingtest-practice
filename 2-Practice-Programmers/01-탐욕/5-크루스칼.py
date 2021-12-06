# [섬 연결하기] 섬을 연결하는 최소비용 (최소신장트리)

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, costs):
    parent = list(range(n))
    edges = [(w, a, b) for a, b, w in costs]

    edges.sort()

    result = 0
    for w, a, b in edges:
        if find(a, parent) != find(b, parent):
            union(a, b, parent)
            result += w

    return result


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))  # 4

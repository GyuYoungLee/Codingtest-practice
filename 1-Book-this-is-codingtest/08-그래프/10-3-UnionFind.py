# [서로소 집합]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = 6
parent = [0, 1, 2, 3, 4, 5, 6]  # 부모 테이블

union(1, 4)
union(2, 3)
union(2, 4)
union(5, 6)

print(parent)  # [0, 1, 1, 2, 1, 5, 5]
print(list(map(find, parent)))  # [0, 1, 1, 1, 1, 5, 5]

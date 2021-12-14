# [여행 계획] 계획의 여행지들이 연결되어 있는지 (서로소집합)

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


n, m = map(int, input().split())
data = [input().split() for _ in range(n)]
plan = list(map(int, input().split()))

parent = list(range(n + 1))

for i in range(n):
    for j in range(n):
        if data[i][j] == '1':
            if find(i) != find(j):
                union(i, j)

result = True
for i in range(m - 1):
    if find(plan[i]) != find(plan[i + 1]):
        result = False

if result:
    print('YES')
else:
    print('NO')

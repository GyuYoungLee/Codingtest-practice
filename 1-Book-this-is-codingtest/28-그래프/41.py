# [여행 계획] 계획의 여행지들이 연결되어 있는지 (서로소집합)

# (아이디어) 연결되어 있으면, 두 여행지를 서로소집합에 포함시킨다

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

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if data[i - 1][j - 1] == '1' and find(i) != find(j):
            union(i, j)

result = 'YES'
for i in range(m - 1):
    if find(plan[i]) != find(plan[i + 1]):
        result = 'NO'
        break
print(result)
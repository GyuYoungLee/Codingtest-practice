# [행성 터널] 모든 행성을 연결하는 최소비용 (크루스칼)

# 두 행성 간 간선을 모두 고려하면 메모리 초과 => 인접한 두 행성 간 간선만 고려한다

import sys


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


n = int(input())
parent = list(range(n))

pos_x = []
pos_y = []
pos_z = []
for i in range(n):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    pos_x.append((x, i))
    pos_y.append((y, i))
    pos_z.append((z, i))

pos_x.sort()
pos_y.sort()
pos_z.sort()

edges = []
for i in range(n - 1):
    edges.append((pos_x[i + 1][0] - pos_x[i][0], pos_x[i + 1][1], pos_x[i][1]))
    edges.append((pos_y[i + 1][0] - pos_y[i][0], pos_y[i + 1][1], pos_y[i][1]))
    edges.append((pos_z[i + 1][0] - pos_z[i][0], pos_z[i + 1][1], pos_z[i][1]))

edges.sort()

cost = 0
for w, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        cost += w

print(cost)

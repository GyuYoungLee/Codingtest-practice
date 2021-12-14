# [행성 터널] 모든 행성을 연결하는 최소비용 (크루스칼)

# 두 행성 간 거리를 모두 구하면 메모리 초과 => 문제 조건에 따라 인접한 행성들간의 간선만 고려한다

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
x = []
y = []
z = []
for i in range(n):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

edges = []
for i in range(n - 1):
    edges.append((x[i+1][0] - x[i][0], x[i+1][1], x[i][1]))  # x축 거리에서 인접한 두 행성
    edges.append((y[i+1][0] - y[i][0], y[i+1][1], y[i][1]))  # y축 거리에서 인접한 두 행성
    edges.append((z[i+1][0] - z[i][0], z[i+1][1], z[i][1]))  # z축 거리에서 인접한 두 행성

edges.sort()

parent = list(range(n))

cost = 0
for w, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        cost += w

print(cost)

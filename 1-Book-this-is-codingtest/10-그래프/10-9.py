# 커리큘럽: 모든 강의를 수강하는 최소시간 (위상정렬)

import collections

N = int(input())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)             # 진입차수 테이블
time = [0] * (N + 1)                 # 강의시간 테이블

for v2 in range(1, N + 1):
    data = list(map(int, input().split()))
    for v1 in data[1:-1]:
        graph[v1].append(v2)
        indegree[v2] += 1
    time[v2] = data[0]

start = [i for i, v in enumerate(indegree) if v == 0 and i != 0]
qu = collections.deque(start)

while qu:
    node = qu.popleft()

    for e in graph[node]:
        indegree[e] -= 1
        if indegree[e] == 0:
            time[e] = time[node] + time[e]
            qu.append(e)

print(time)  # [0, 10, 20, 14, 18, 17]

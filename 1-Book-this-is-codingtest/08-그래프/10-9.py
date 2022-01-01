# [커리큘럽] 모든 강의를 수강하는 최소시간 (위상정렬)

import collections
import copy

n = int(input())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)    # 진입차수 테이블
time = [0] * (n + 1)        # 강의시간 테이블

for b in range(1, n + 1):
    data = list(map(int, input().split()))
    for a in data[1:-1]:
        graph[a].append(b)
        indegree[b] += 1
    time[b] = data[0]

start = [i for i, x in enumerate(indegree) if x == 0 and i != 0]
qu = collections.deque(start)
result = copy.deepcopy(time)

while qu:
    now = qu.popleft()

    for e in graph[now]:
        indegree[e] -= 1
        result[e] = max(result[e], result[now] + time[e])
        if indegree[e] == 0:
            qu.append(e)

print(result)  # [0, 10, 20, 14, 18, 17]

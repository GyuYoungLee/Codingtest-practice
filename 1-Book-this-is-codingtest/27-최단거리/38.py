# [정확한 순위] 순위를 알수있는 학생의 수 (플로이드워셜)

import sys

n, m = map(int, input().split())

score = [[0] * (n + 1) for _ in range(n + 1)]

# 직접 승부 결과 업데이트 => 1 (승), -1 (패), 0 (모름)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    score[a][b] = -1
    score[b][a] = 1

# 간접 승부 결과 업데이트 => (플로이드워셜) i -> k -> j
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if score[i][k] and score[k][j]:
                if score[i][k] == score[k][j]:
                    score[i][j] = score[i][k]
                    score[j][i] = -score[i][k]

# 모든 사람과의 승부 결과가 있는 학생 카운트
count = 0
for i in range(1, n + 1):
    f = score[i][1:]
    if len([x for x in f if x != 0]) == n - 1:
        count += 1

print(count)

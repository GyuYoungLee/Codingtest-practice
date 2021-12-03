# [순위] 순위를 매길수 있는 선수의 수 (플로이드워셜)

# 순위를 매길수 있는 선수 ?? 모든 사람과의 승부 결과를 직접 또는 간접적으로 알수 있는 선수

def solution(n, results):
    # 1 (승), -1 (패), 0 (모름)
    dist = [[0] * n for _ in range(n)]
    for win, lose in results:
        dist[win-1][lose-1] = 1
        dist[lose-1][win-1] = -1

    # 간접 승부 결과 업데이트 => (플로이드워셜) i -> k -> j
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j and dist[i][k] and dist[k][j]:
                    if dist[i][k] == dist[k][j]:
                        dist[i][j] = dist[i][k]
                        dist[j][i] = -dist[i][k]

    # 모든 사람과의 승부 결과가 있는 선수 카운트
    count = 0
    for i, a in enumerate(dist):
        if all(x != 0 for x in a[:i] + a[i+1:]):
            count += 1
    return count


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

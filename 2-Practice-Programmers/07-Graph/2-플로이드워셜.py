# [순위] 순위를 매길수 있는 선수의 수 (플로이드워셜)

# 순위를 매길수 있는 선수 ?? 모든 사람과의 승부 결과를 직접 또는 간접적으로 알수 있는 선수

def solution(n, results):
    score = [[0] * (n + 1) for _ in range(n + 1)]

    # 직접 승부 결과 업데이트 => 1 (승), -1 (패), 0 (모름)
    for w, l in results:
        score[w][l] = 1
        score[l][w] = -1

    # 간접 승부 결과 업데이트 => (플로이드워셜) i -> k -> j
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i != j and score[i][k] and score[k][j]:
                    if score[i][k] == score[k][j]:
                        score[i][j] = score[i][k]
                        score[j][i] = -score[i][k]

    # 모든 사람과의 승부 결과가 있는 선수 카운트
    count = 0
    for arr in score[1:]:
        if len([x for x in arr[1:] if x != 0]) == n - 1:
            count += 1
    return count


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

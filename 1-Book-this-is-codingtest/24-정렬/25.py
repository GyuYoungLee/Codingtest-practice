# [실패율] 실패율 역순으로 정렬 (정렬)

def solution(n, stages):
    fail_rate = []
    stages.sort(reverse=True)
    # stages: [6, 4, 3, 3, 2, 2, 2, 1]

    # stage 1 에서 stage n 까지 실패율 계산
    for i in range(1, n + 1):
        n = len(stages)

        if not stages:
            fail_rate.append((i, 0))
            continue

        count = 0
        while stages and stages[-1] == i:
            stages.pop()
            count += 1

        fail_rate.append((i, count / n))

    # 실패율 역순으로 정렬
    return [i for i, r in sorted(fail_rate, key=lambda x: (-x[1], x[0]))]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

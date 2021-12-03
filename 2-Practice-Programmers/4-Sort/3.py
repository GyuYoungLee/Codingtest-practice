# [H-index] 최대 H-index 리턴 (정렬)

def solution(citations):
    # arr: [6, 5, 3, 1, 0]
    citations = sorted(citations, reverse=True)
    n = len(citations)

    # 효율성을 위해 큰 값부터 확인후 조기리턴 하도록 구현
    for i in range(n, 0, -1):
        if citations[i - 1] >= i:
            return i

    return 0


print(solution([3, 0, 6, 1, 5]))  # 3

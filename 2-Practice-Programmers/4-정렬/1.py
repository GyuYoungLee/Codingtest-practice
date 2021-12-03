# [K번째수] 연산결과 리턴 (정렬)

def solution(array, commands):
    result = []

    for i, j, k in commands:
        num = sorted(array[i - 1:j])[k - 1]
        result.append(num)

    return result


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))  # [5, 6, 3]

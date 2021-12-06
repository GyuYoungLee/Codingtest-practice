# [모의고사] 가장 많은 문제를 맞힌 사람이 누구인지 (완전탐색)

def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]

    # (완전탐색)
    for i, x in enumerate(answers):
        if x == first[i % len(first)]:
            score[0] += 1
        if x == second[i % len(second)]:
            score[1] += 1
        if x == third[i % len(third)]:
            score[2] += 1

    result = [i + 1 for i, x in enumerate(score) if x == max(score)]
    return result


print(solution([1, 2, 3, 4, 5]))  # [1]
print(solution([1, 3, 2, 4, 2]))  # [1, 2, 3]

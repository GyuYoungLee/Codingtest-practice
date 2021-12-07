# 구현

def solution(n):
    pattern = '수박'

    answer = ''
    for i in range(n):
        answer += pattern[i % 2]

    return answer


print(solution(3))

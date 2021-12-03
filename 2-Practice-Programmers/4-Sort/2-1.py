# [가장 큰 수] 가장 큰수를 만들어서 문자열로 리턴 (정렬)

# 끝자리를 늘려서 4자리 수로 비교하는 방식은 정답이 아니다 [30, 3021] => 3000, 3021 => 3021 30 (X)
# 전체를 늘려서 *3 수로 비교해야 한다 [30, 3021] => 303030, 302130213021      => 30 3021 (O)

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int("".join(numbers)))


print(solution([6, 10, 2]))  # 6210
print(solution([3, 30, 34, 5, 9]))  # 9534330
print(solution([30, 3021]))  # 303021 => 1-6 반례
print(solution([0, 0]))  # 0 => 18번 반례

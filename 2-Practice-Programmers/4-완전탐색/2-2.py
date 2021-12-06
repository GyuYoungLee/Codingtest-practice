# [소수 찾기] 소수를 몇개 만들수 있는지 (완전탐색, 재귀)

def is_prime(n):
    return all(n % i for i in range(2, int(n ** 0.5) + 1)) and n >= 2


def solution(numbers):
    result = set()

    def dfs(a, target):
        if target != '':
            if is_prime(int(target)):
                result.add(int(target))

        n = len(a)  # 입력값 a 에 따라 반복횟수가 달라진다
        for i in range(n):
            dfs(a[:i] + a[i + 1:], target + a[i])

    dfs(numbers, '')
    return len(result)


print(solution("17"))  # 3
print(solution("011"))  # 2

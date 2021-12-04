# [N으로 표현] 숫자 사용횟수의 최소값 (dp)

# dp = [0, [n], [n을 2개 사용 리스트], [n을 3개 사용 리스트], ...]

def solution(n, number):
    if n == number:
        return 1

    dp = [0, [n]]

    for i in range(2, 9):
        # n 숫자를 i번 사용해서 만들수 있는 모든 숫자를 구한다
        temp = set()
        temp.add(int(str(n) * i))

        for j in range(1, len(dp)):
            for x in dp[j]:
                for y in dp[i - j]:
                    temp.add(x + y)
                    temp.add(x * y)
                    temp.add(x - y)
                    temp.add(y - x)
                    if y != 0:
                        temp.add(x // y)
                    if x != 0:
                        temp.add(y // x)

        if number in temp:
            return i

        dp.append(list(temp))

    return -1


print(solution(5, 12))  # 4
print(solution(2, 11))  # 3
print(solution(5, 5))  # 1 => 9번 반례

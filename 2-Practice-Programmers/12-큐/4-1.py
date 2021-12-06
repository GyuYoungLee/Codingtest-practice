# [주식가격] 가격이 떨어지지 않은 기간은 몇 초인지 (투 포인터)


def solution(prices):
    result = []
    n = len(prices)
    i = 0

    while i < n:
        count = 0
        j = i + 1

        while j < n:
            count += 1
            if prices[j] < prices[i]:
                break
            j += 1

        result.append(count)
        i += 1

    return result


print(solution([1, 2, 3, 2, 3]))  # [4, 3, 1, 1, 0]

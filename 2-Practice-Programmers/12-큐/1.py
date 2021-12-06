# [주식가격] 가격이 떨어지지 않은 기간은 몇 초인지 (큐)

import collections


def solution(prices):
    result = []
    qu = collections.deque(prices)

    while qu:
        x = qu.popleft()
        
        count = 0
        for i in qu:
            count += 1
            if i < x:
                break
        
        result.append(count)

    return result


print(solution([1, 2, 3, 2, 3]))  # [4, 3, 1, 1, 0]

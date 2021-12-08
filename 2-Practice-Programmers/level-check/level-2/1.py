# 탐욕

import collections


def solution(people, limit):
    qu = collections.deque(sorted(people))
    answer = 0

    while qu:
        # (탐욕) 가장 무거운 사람과 가장 가벼운 사람을 보트에 태운다
        if len(qu) >= 2 and qu[0] + qu[-1] <= limit:
            qu.popleft()
            qu.pop()

        # (탐욕) 가장 무서운 사람을 보트에 태운다
        else:
            qu.pop()

        answer += 1

    return answer


print(solution([70, 50, 80, 50], 100))  # 3
print(solution([70, 80, 50], 100))  # 3

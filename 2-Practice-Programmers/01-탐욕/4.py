# [구명보트] 필요한 구명보트 개수의 최소값 (탐욕)

import collections


def solution(people, limit):
    count = 0
    qu = collections.deque(sorted(people))

    while qu:
        # (탐욕) 가장 무거운 사람과 가장 가벼운 사람을 같이 타게 한다
        if len(qu) >= 2 and qu[-1] + qu[0] <= limit:
            qu.popleft()
            qu.pop()
        else:
            qu.pop()
        count += 1

    return count


print(solution([70, 50, 80, 50], 100))  # 3
print(solution([70, 80, 50], 100))  # 3

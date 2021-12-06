# [다리를 지나는 트럭] 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 (큐)

# 시간 초과 => total 변수에 저장해서 sum() 연산을 제거함

import collections


def solution(bridge_length, weight, truck_weights):
    bridge = collections.deque([0] * bridge_length)
    truck = collections.deque(truck_weights)
    time = 0
    total = 0

    # bridge: [0, 0], truck: [7, 4, 5, 6]
    while bridge:
        time += 1
        o = bridge.popleft()
        total -= o

        if truck:
            if total + truck[0] <= weight:
                i = truck.popleft()
                bridge.append(i)
                total += i
            else:
                bridge.append(0)

    return time


print(solution(2, 10, [7, 4, 5, 6]))  # 8
print(solution(100, 100, [10]))  # 101
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))  # 110

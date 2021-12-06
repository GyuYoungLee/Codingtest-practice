# [위장] 서로 다른 옷의 조합의 수 (dict)

import collections


def solution(clothes):
    clothes_by_kind = collections.defaultdict(list)
    for name, kind in clothes:
        clothes_by_kind[kind].append(name)

    # clothes_by_kind: {'headgear': ['yellow_hat', 'green_turban'], 'eyewear': ['blue_sunglasses']}

    result = 1
    for _, v in clothes_by_kind.items():
        result *= len(v) + 1

    return result - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))  # 5
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))  # 3

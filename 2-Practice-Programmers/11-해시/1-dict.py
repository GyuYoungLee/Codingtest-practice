# [완주하지 못한 선수] 완주하지 못한 선수의 이름 (dict)

import collections


def solution(start_list, end_list):
    counts = collections.defaultdict(int)

    for name in start_list:
        counts[name] += 1

    for name in end_list:
        counts[name] -= 1

    # counts: {'leo': 1, 'kiki': 0, 'eden': 0}
    return [name for name in counts if counts[name] == 1][0]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))  # leo
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))  # vinko
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))  # mislav

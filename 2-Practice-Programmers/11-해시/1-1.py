# [완주하지 못한 선수] 완주하지 못한 선수의 이름 (dict)

import collections


def solution(start_list, end_list):
    counts = collections.Counter(start_list) - collections.Counter(end_list)
    return list(counts.keys())[0]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

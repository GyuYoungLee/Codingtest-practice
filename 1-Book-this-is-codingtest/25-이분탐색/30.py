# [가사 검색] 매치된 단어의 개수 (이분탐색) <= 정규식으로 풀면 시간초과

import collections
import bisect


def solution(words, queries):
    result = []
    a1 = collections.defaultdict(list)
    a2 = collections.defaultdict(list)
    for w in words:
        n = len(w)
        a1[n].append(w)
        a2[n].append(w[::-1])

    # 이분탐색을 위한 정렬
    for n in a1:
        a1[n].sort()
        a2[n].sort()

    for q in queries:
        n = len(q)
        if q[-1] == '?':
            left = bisect.bisect_left(a1[n], q.replace('?', 'a'))
            right = bisect.bisect_right(a1[n], q.replace('?', 'z'))
        else:
            left = bisect.bisect_left(a2[n], q[::-1].replace('?', 'a'))
            right = bisect.bisect_right(a2[n], q[::-1].replace('?', 'z'))

        result.append(right - left)

    return result


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))

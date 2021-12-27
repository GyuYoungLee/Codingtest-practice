# [가사 검색] 매치된 단어의 개수 (이분탐색) <= 정규식으로 풀면 시간초과

# (아이디어) "fro??" => 길이가 5이고, froaa <= x <= frozz 인지 확인한다

import collections
import bisect


def solution(words, queries):
    result = []
    d1 = collections.defaultdict(list)
    d2 = collections.defaultdict(list)

    for w in words:
        d1[len(w)].append(w)
        d2[len(w)].append(w[::-1])

    # 이분탐색을 위한 정렬
    for i in d1:
        d1[i].sort()
        d2[i].sort()

    for q in queries:
        if q[-1] == '?':
            left = bisect.bisect_left(d1[len(q)], q.replace('?', 'a'))
            right = bisect.bisect_right(d1[len(q)], q.replace('?', 'z'))
        else:
            left = bisect.bisect_left(d2[len(q)], q[::-1].replace('?', 'a'))
            right = bisect.bisect_right(d2[len(q)], q[::-1].replace('?', 'z'))

        result.append(right - left)

    return result


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))

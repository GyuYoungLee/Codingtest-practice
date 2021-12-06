# [베스트앨범] 베스트 앨범에 수록될 노래의 고유번호의 순서 (dict)

import collections


def solution(genres, plays):
    data = collections.defaultdict(list)
    for g, p, i in zip(genres, plays, range(len(genres))):
        data[g].append((p, i))

    # 많이 재생된 노래, 번호가 낮은 노래 순으로 정렬
    # {'classic': [(800, 3), (500, 0), (150, 2)], 'pop': [(2500, 4), (600, 1)]})
    for k, v in data.items():
        v.sort(key=lambda x: (-x[0], x[1]))

    # 많이 재생된 장르 순으로 정렬
    # ['pop', 'classic']
    most_genres = sorted(data, key=lambda x: sum([p for p, i in data[x]]), reverse=True)

    result = []
    for g in most_genres:
        for _, i in data[g][:2]:
            result.append(i)

    return result


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))  # [4, 1, 3, 0]

# [방의 개수] 방의 개수 (시뮬레이션)

# 재방문 정점이 생길 때마다 방이 생성된다
# (예외처리) 방이 2개 생성되는 경우 => 이동경로를 2배로 가정한다


def solution(arrows):
    move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    visited = set()
    visited_edges = set()

    v = (0, 0)
    visited.add(v)

    count = 0
    for d in arrows:
        # (예외처리) 방이 2개 생성되는 경우 => 이동경로를 2배로 가정한다
        for _ in range(2):
            nv = (v[0] + move[d][0], v[1] + move[d][1])

            # 재방문 정점이 생길 때마다 방이 생성된다
            if nv in visited and (v, nv) not in visited_edges:
                count += 1

            visited.add(nv)
            visited_edges.add((v, nv))
            visited_edges.add((nv, v))
            v = nv

    return count


print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))  # 3

# [방의 개수] 방의 개수 (시뮬레이션)

def solution(arrows):
    move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    visited = set()
    visited_edges = set()

    x = 0
    y = 0
    visited.add((0, 0))

    count = 0
    for d in arrows:
        # (예외처리) 방이 2개 생성되는 경우 => 이동경로를 2배로 가정한다
        for _ in range(2):
            nx = x + move[d][0]
            ny = y + move[d][1]

            # 재방문 정점이 생길 때마다 방이 생성된다
            if (nx, ny) in visited and (x, y, nx, ny) not in visited_edges:
                count += 1

            visited.add((nx, ny))
            visited_edges.add((x, y, nx, ny))
            visited_edges.add((nx, ny, x, y))
            x = nx
            y = ny

    return count


print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))  # 3

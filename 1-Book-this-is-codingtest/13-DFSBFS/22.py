# [블록 이동하기] 이동횟수 (BFS)

# (아이디어) 정점을 set()으로 표현 => {(1, 1), (1, 2)}

# 탐색 방향: 상하좌우
# 탐색 조건: e not in visited, board[x][y] == 0
# 탐색 결과: visited.append(e)

import collections


def get_next(now, board):
    result = []
    now = list(now)
    x1, y1, x2, y2 = now[0][0], now[0][1], now[1][0], now[1][1]

    # 이동
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx1 = x1 + dx
        ny1 = y1 + dy
        nx2 = x2 + dx
        ny2 = y2 + dy
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            result.append({(nx1, ny1), (nx2, ny2)})

    # 회전 - 로봇이 가로로 놓인 경우
    if x1 == x2:
        # 아래쪽
        if board[x1 - 1][y1] == 0 and board[x2 - 1][y2] == 0:
            result.append({(x1, y1), (x1 - 1, y1)})
            result.append({(x2, y2), (x2 - 1, y2)})
        # 위쪽
        if board[x1 + 1][y1] == 0 and board[x2 + 1][y2] == 0:
            result.append({(x1, y1), (x1 + 1, y1)})
            result.append({(x2, y2), (x2 + 1, y2)})

    # 회전 - 로봇이 세로로 놓인 경우
    if y1 == y2:
        # 왼쪽
        if board[x1][y1 - 1] == 0 and board[x2][y2 - 1] == 0:
            result.append({(x1, y1), (x1, y1 - 1)})
            result.append({(x2, y2), (x2, y2 - 1)})
        # 오른쪽
        if board[x1][y1 + 1] == 0 and board[x2][y2 + 1] == 0:
            result.append({(x1, y1), (x1, y1 + 1)})
            result.append({(x2, y2), (x2, y2 + 1)})

    return result


def solution(board):
    n = len(board)

    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    s = {(1, 1), (1, 2)}
    qu = collections.deque([(s, 0)])
    visited = [s]

    while qu:
        now, count = qu.popleft()

        if (n, n) in now:
            return count

        for e in get_next(now, new_board):
            if e not in visited:
                visited.append(e)
                qu.append((e, count + 1))

    return -1


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))

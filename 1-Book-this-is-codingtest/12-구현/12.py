# [기둥과 보 설치] 조건을 만족하는 작업목록 리턴 (구현, 시뮬레이션)

def is_possible(result):
    for x, y, stuff in result:
        # 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위
        if stuff == 0:
            if y == 0:
                continue
            elif (x - 1, y, 1) in result or (x, y, 1) in result:
                continue
            elif (x, y - 1, 0) in result:
                continue
            return False

        # 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어
        else:
            if (x, y - 1, 0) in result or (x + 1, y - 1, 0) in result:
                continue
            elif (x - 1, y, 1) in result and (x + 1, y, 1) in result:
                continue
            return False

    return True


def solution(n, build_frame):
    result = []
    for x, y, stuff, op in build_frame:
        if op == 1:
            result.append((x, y, stuff))
            if not is_possible(result):
                result.remove((x, y, stuff))
        else:
            result.remove((x, y, stuff))
            if not is_possible(result):
                result.append((x, y, stuff))

    return sorted(result)


plan = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1]]
plan += [[5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
print(solution(5, plan))
plan = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1]]
plan += [[2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
print(solution(5, plan))

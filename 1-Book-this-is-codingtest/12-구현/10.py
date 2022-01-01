# [자물쇠와 열쇠] 열쇠와 자물쇠를 합쳐서 맞는지 확인 (구현, 완전탐색)

def rotate_90(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][(n - 1) - i] = a[i][j]
    return result


def check(new_lock, n):
    for i in range(n, n * 2):
        for j in range(n, n * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)

    # (TIP) key를 맞춰보기 위해 lock을 3배 늘린다
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 회전하고 탐색
    for _ in range(4):
        key = rotate_90(key)

        # 이동하며 탐색
        for x in range(n * 2):
            for y in range(n * 2):

                # 열쇠 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[i + x][j + y] += key[i][j]
                # 검사
                if check(new_lock, n):
                    return True

                # 열쇠 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[i + x][j + y] -= key[i][j]

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

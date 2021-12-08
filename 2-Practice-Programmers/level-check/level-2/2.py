# 구현

def solution(n):
    arr = [[0] * (i + 1) for i in range(n)]
    move = [(1, 0), (0, 1), (-1, -1)]

    x = -1
    y = 0
    turns = 0
    num = 1

    while n > 0:

        for _ in range(n):
            x += move[turns % 3][0]
            y += move[turns % 3][1]

            arr[x][y] = num
            num += 1

        # 반복할 때마다 패턴과 길이가 달라진다
        turns += 1
        n -= 1

    result = [num for a in arr for num in a]
    return result


print(solution(5))

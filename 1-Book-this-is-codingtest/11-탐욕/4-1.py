# [만들 수 없는 금액] 만들 수 없는 금액 중 최소값 (DP)

a = [1, 1, 2, 3, 9]
dp = [[], [a[0]]]
# [[], [1], [1, 2], [1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16]]

for i in range(2, len(a) + 1):

    # 만들수 있는 모든 숫자 구하기
    temp = set(dp[i - 1])

    new = a[i - 1]
    temp.add(new)
    temp |= set([x + new for x in dp[i - 1]])

    # 결과에서 빠진 숫자 출력
    stop = False
    for x in range(1, max(temp)):
        if x not in temp:
            print(x)
            stop = True
            break
    if stop:
        break

    dp.append(list(temp))

# [연산자 끼워 넣기] 만들수 있는 식 중에 최대값과 최소값 (재귀=순열)

# practice-programmers-dfs-1 비교

n = int(input())
a = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_v = int(1e9)
max_v = -int(1e9)


def solution(num, idx):
    global add, sub, mul, div, min_v, max_v

    if idx == n:
        min_v = min(min_v, num)
        max_v = max(max_v, num)
        return

    if add > 0:
        add -= 1
        solution(num + a[idx], idx + 1)
        add += 1

    if sub > 0:
        sub -= 1
        solution(num - a[idx], idx + 1)
        sub += 1

    if mul > 0:
        mul -= 1
        solution(num * a[idx], idx + 1)
        mul += 1

    if div > 0:
        div -= 1
        solution(int(num / a[idx]), idx + 1)
        div += 1


solution(a[0], 1)
print(max_v)
print(min_v)

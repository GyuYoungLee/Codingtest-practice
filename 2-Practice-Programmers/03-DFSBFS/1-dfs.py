# [타켓 넘버] 숫자를 만드는 모든 경우의 수 (재귀)

def solution(arr, target):
    count = 0

    def dfs(num, idx):
        nonlocal count
        if idx == len(arr):
            if num == target:
                count += 1
            return

        dfs(num + arr[idx], idx + 1)
        dfs(num - arr[idx], idx + 1)

    dfs(0, 0)
    return count


print(solution([1, 1, 1, 1, 1], 3))  # 5

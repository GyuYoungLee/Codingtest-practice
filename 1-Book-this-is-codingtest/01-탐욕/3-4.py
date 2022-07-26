# [1이 될때까지] 최소 연산횟수 (탐욕 or DP)

n, k = map(int, input().split())
count = 0

# 풀이 1
while n != 1:

    if n % k == 0:
        n //= k
        count += 1
        
    else:
        n -= 1
        count += 1

print(count)  # 3

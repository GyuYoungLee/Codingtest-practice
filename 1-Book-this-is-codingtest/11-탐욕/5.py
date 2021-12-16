# [볼링공 고르기] 볼링공을 고르는 경우의 수 (탐욕)

# (아이디어) 모든 무게의 볼링공에 대해 케이스를 고려한다

n, m = map(int, input().split())
a = list(map(int, input().split()))

by_w = [0] * (m + 1)
for x in a:
    by_w[x] += 1

count = 0
for i in range(1, m + 1):
    n -= by_w[i]
    count += by_w[i] * n

print(count)

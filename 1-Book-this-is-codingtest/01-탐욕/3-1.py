# [거스름돈] 거스름 동전의 최소 갯수 (탐욕)

n = 1260
count = 0

coin_type = [500, 100, 50, 10]  # 큰 동전으로 먼저 선택

for coin in coin_type:
    count += n // coin
    n %= coin

print(count)  # 6

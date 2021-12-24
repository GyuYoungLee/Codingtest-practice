# [큰수의 법칙] m번 선택해서 만들어지는 가장 큰수 (탐욕)

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
*_, second, first = data

# 풀이 2 (개선)
first_cnt = m // (k + 1) * k + m % (k + 1)
second_cnt = m // (k + 1)

result = first * first_cnt + second * second_cnt

print(result)  # 46

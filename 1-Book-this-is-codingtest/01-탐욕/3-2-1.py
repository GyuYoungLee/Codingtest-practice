# [큰수의 법칙] m번 선택해서 만들어지는 가장 큰수 (탐욕)

n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)
first, second, *_ = numbers

# 풀이 2 (개선)

# 6 6 6 5 6 6 6 5 => (6 6 6 5) * 2
repeat_times = m // (k + 1)
rest_count_of_first = m % (k + 1)

result = (first * k + second) * repeat_times
result += first * rest_count_of_first

print(result)

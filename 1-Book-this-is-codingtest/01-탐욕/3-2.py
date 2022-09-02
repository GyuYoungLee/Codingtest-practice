# [큰수의 법칙] m번 선택해서 만들어지는 가장 큰수 (탐욕)

n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)
first, second, *_ = numbers

# 풀이 1
result = 0
while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1

    if m == 0:
        break
    result += second
    m -= 1

print(result)  # 46

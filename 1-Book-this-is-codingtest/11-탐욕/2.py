# [곱하기 혹은 더하기] 만들수 있는 가장 큰 수 (탐욕)

# (아이디어) 더하기보다 곱하기를 한다

a = list(map(int, input()))

result = a[0]

for i in range(1, len(a)):
    current = a[i]

    if result in [0, 1] or current in [0, 1]:
        result += current
    else:
        result *= current

print(result)

# [문자열 뒤집기] 뒤집기 최소횟수 (탐욕)

# (아이디어) 01 또는 10 횟수를 센다

a = input()
count0 = 0  # 전부 0으로 바꾸는 경우
count1 = 0  # 전부 1로 바꾸는 경우

if a[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(a) - 1):
    cur = a[i:i + 2]

    if cur == '01':
        count0 += 1
    elif cur == '10':
        count1 += 1

print(min(count0, count1))

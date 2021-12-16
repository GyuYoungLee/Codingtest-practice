# [모험가 길드] 만들수 있는 그룹의 최대수 (탐욕)

# (아이디어) 작은 그룹부터 생성한다

n = int(input())
a = list(map(int, input().split()))

a.sort()

group = 0
count = 0

for x in a:
    count += 1
    if count >= x:
        group += 1
        count = 0

print(group)

# [만들 수 없는 금액] 만들 수 없는 금액 중 최소값 (탐욕)

# (아이디어) [1, 4] => 4 가 추가되면 최대 가능한 수 1 보다 크기 때문에 2, 3 을 만들수 없다
#                 => 최대 가능한 수만 계산한다

n = int(input())
a = list(map(int, input().split()))
a.sort()

possible_max = a[0]
for x in a[1:]:
    if x > possible_max:
        break
    possible_max += x

print(possible_max + 1)

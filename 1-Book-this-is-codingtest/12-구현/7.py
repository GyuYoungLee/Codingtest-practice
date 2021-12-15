# [럭키 스트레이드] 럭키 스트레이트 상태인지 확인 (구현)

a = list(map(int, list(input())))
n = len(a)

left = sum(a[:n // 2])
right = sum(a[n // 2:])

if left == right:  # 럭키 스트레이트 상태
    print('LUCKY')
else:
    print('READY')

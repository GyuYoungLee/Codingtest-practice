# [문자열 재정렬] 문자와 숫자 분리해서 각각 변환 후 결과 출력 (구현)

ar = input()

alpha = []
num = 0

for ch in ar:
    if ch.isalpha():
        alpha.append(ch)
    else:
        num += int(ch)

result = sorted(alpha) + [str(num)]
print(''.join(map(str, result)))

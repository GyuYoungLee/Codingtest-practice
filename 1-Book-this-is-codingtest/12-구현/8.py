# [문자열 재정렬] 문자와 숫자 분리해서 각각 변환 후 결과 출력 (구현)

ar = input()

alpha = []
num = []

for ch in ar:
    if ch.isalpha():
        alpha.append(ch)
    else:
        num.append(int(ch))

result = sorted(alpha) + ([str(sum(num))] if num else [])
print(''.join(result))

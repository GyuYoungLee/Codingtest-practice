# [문자열 압축] 문자열 압축 표현식 중 최소길이 (구현)

def solution(s):
    n = len(s)
    min_v = n

    for w in range(1, n // 2 + 1):
        compressed = ''
        x = s[:w]
        count = 1

        for i in range(w, n, w):
            e = s[i:i + w]

            if e == x:
                count += 1
            else:
                compressed += str(count) + x if count >= 2 else x
                x = s[i:i + w]
                count = 1

        # 마지막 비교 단어 처리
        compressed += str(count) + x if count >= 2 else x
        min_v = min(min_v, len(compressed))

    return min_v


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))

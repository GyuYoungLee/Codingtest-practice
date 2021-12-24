# [문자열 압축] 문자열 압축 표현식 중 최소길이 (구현, 완전탐색)

def solution(s):
    n = len(s)
    min_v = n

    # 압축 길이를 늘려가며 완전탐색
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
                x = e
                count = 1

        # 마지막으로 비교된 문자열 추가
        compressed += str(count) + x if count >= 2 else x
        min_v = min(min_v, len(compressed))

    return min_v


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))

# 구현

def solution(s):
    result = ''.join(sorted(list(s), reverse=True))
    return result


print(solution('Zbcdefg'))  # gfedcbZ

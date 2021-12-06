# [조이스틱] 조이스틱 조작횟수의 최소값 (탐욕)

# name 에 'A' 문자가 포함되어 있으면 변경할 필요가 없다는 것이 풀이의 핵심포인트

def solution(name):
    n = len(name)
    v_cnt = 0  # up, down
    h_cnt = n - 1  # right, left

    for i, x in enumerate(name):
        up = ord(x) - ord('A')
        down = ord('Z') - ord(x) + 1
        v_cnt += min(up, down)

        # "JJAAAAZZ" => right = 1, left = 3
        a_idx = i + 1
        while a_idx < n and name[a_idx] == 'A':
            a_idx += 1

        right = i
        left = i + (n - a_idx)
        h_cnt = min(h_cnt, right + left)  # (탐욕) 최소한의 조작횟수

    return v_cnt + h_cnt


print(solution("JAZ"))  # 11
print(solution("JEROEN"))  # 56
print(solution("JAN"))  # 23

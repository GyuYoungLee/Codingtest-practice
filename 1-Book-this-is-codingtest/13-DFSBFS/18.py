# [괄호 변환] "균형잡힌 괄호 문자열"을 "올바른 괄호 문자열"로 변환하기 (재귀)

# 균형잡힌 괄호 문자열
def get_balanced(a):
    cnt = 0
    for i in range(len(a)):
        if a[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return a[:i + 1], a[i + 1:]


# 균형잡힌 문자열이 올바른 문자열인지 체크
def is_proper(a):
    st = []
    for ch in a:
        if ch == '(':
            st.append(ch)
        else:
            if st and st[-1] == '(':
                st.pop()
            else:
                return False
    return True


def solution(p):
    def dfs(p):
        # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다
        if not p:
            return p

        # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다
        u, v = get_balanced(p)

        # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다
        if is_proper(u):
            return u + dfs(v)

        # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면
        else:
            return '(' + dfs(v) + ')' + u[1:-1].replace('(', '-').replace(')', '(').replace('-', ')')

    result = dfs(p)
    return result


print(solution("()))((()"))

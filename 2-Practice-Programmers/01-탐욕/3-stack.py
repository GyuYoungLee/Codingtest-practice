# [큰 수 만들기] 만들수 있는 가장 큰수 (탐욕)

def solution(number, k):
    st = []

    for num in number:

        # (탐욕) 앞의 숫자가 작으면 제거한다
        while k > 0 and st and st[-1] < num:
            st.pop()
            k -= 1

        st.append(num)

    while k > 0:
        st.pop()
        k -= 1

    return ''.join(st)


print(solution('1924', 2))  # "94"
print(solution('1231234', 3))  # "3234"
print(solution('4177252841', 4))  # "775841"
print(solution('999', 2))  # "9" => 12번 반례

# [전화번호 목록] 어떤 번호가 다른 번호의 접두어이면 false 리턴 (set)

def solution(phone_book):
    phone_book = set(phone_book)

    for phone in phone_book:
        target = ''
        for ch in phone[:-1]:
            target += ch
            if target in phone_book:
                return False

    return True


print(solution(["119", "97674223", "1195524421"]))  # false
print(solution(["123", "456", "789"]))  # true
print(solution(["12", "123", "1235", "567", "88"]))  # false

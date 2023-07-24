def solution(phone_book):
    phone_book.sort()
    for i, phone in enumerate(phone_book):
        while True:
            if i < len(phone_book) - 1: i += 1
            else: break
            if len(phone) >= len(phone_book[i]):break
            if phone[-1] != phone_book[i][len(phone)-1]:break
            if phone == phone_book[i][:len(phone)]:return False
    return True
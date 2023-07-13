def solution(enroll, referral, seller, amount):
    hash_e = dict(zip(enroll, referral))
    result = dict.fromkeys(enroll, 0)
    for s, a in zip(seller, amount):
        a *= 100
        while s != "-" and a:
            py_a = a // 10
            a -= py_a
            result[s] += a
            s, a = hash_e.get(s), py_a
    return list(result.values())
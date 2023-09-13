import re
def solution(n, k):
    nums = []
    s = ""
    while n:
        n, m = divmod(n, k)
        s = str(m) + s
        
    def isprime(n):
        if not n or n == '1':
            return False
        n = int(n)
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return sum(map(isprime, re.split('0+', s)))
def solution(n):
    answer = 0
    for s in range(1, n+1):
        S = 0
        for e in range(s, n+1):
            S += e
            if S == n:
                answer += 1
            if S >= n:
                break
    return answer


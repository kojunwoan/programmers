def solution(land):
    score = [0 for _ in range(4)]
    for row in land:
        score = [row[i] + max(score[:i] + score[i+1:]) for i in range(4)]
    return max(score)
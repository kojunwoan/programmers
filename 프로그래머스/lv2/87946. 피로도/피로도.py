def solution(k, dungeons):
    return max([solution(k - con, dungeons[:i] + dungeons[i+1:]) + 1 for i, (lea, con) in enumerate(dungeons) if k >= lea] or [0])
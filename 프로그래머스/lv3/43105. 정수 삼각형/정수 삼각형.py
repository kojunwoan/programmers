def solution(triangle):
    for m_row, c_row in zip(triangle[-2::-1], triangle[-1::-1]):
        for i, c in enumerate(zip(c_row[:-1], c_row[1:])):
            m_row[i] += max(c)
    return triangle[0][0]
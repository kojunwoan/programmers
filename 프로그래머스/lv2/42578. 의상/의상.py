from collections import Counter
from functools import reduce
def solution(clothes):
    count = Counter(c for _, c in clothes)
    res = reduce(lambda x, y: x * (y + 1), count.values(), 1)
    return res - 1
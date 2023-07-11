import re
from collections import Counter
def solution(str1, str2):
    c = [Counter(sum([re.findall('\w{2}', w) + re.findall('\w{2}', w[1:]) for w in re.findall('[a-z]{2,}', s.lower())], [])) for s in [str1, str2]]
    j = sum((c[0]&c[1]).values()) / sum((c[0]|c[1]).values()) if any(c) else 1
    return (j * 65536).__int__()
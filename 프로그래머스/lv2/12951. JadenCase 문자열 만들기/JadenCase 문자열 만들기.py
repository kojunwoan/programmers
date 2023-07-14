import re
def solution(s):
    return re.sub('\w{1,}', lambda x: x.group().capitalize(), s)
def solution(s):
    s = sorted(map(lambda ss: list(map(int, ss.replace('}','').split(','))), s[:-2].replace('{','').split('},')), key=len)
    answer = []
    for ss in s:
        answer.extend(list(set(ss) - set(answer)))
    return answer
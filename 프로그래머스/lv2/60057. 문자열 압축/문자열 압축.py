def solution(s):
    dic = {i : "" for i in range(1, len(s) + 1)}
    for i in range(1, len(s) + 1):
        cnt = 1
        div, no_s, re_s = "", "", s
        while no_s or re_s:
            no_s, re_s = re_s[:i], re_s[i:]
            if div != no_s:
                dic[i] += div if cnt == 1 else str(cnt) + div
                div = no_s
                cnt = 1
            else:
                cnt += 1
    return min([len(i) for i in dic.values()])
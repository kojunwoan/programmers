def solution(s):
    st = []
    for i in s:
        if i == '(':
            st.append(i)
        else:
            if not st:
                return False
            st.pop()

    return not st
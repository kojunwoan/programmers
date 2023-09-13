def solution(prices):
    st, du = [], [0 for _ in prices]
    for i, p in enumerate(prices):
        while st and st[-1][1] > p:
            li, lp = st.pop()
            du[li] = i - li
        st.append((i, p))
    for li, lp in st:
        du[li] = i - li
    return du
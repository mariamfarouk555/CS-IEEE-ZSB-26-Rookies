t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    st = set()
    ans = 0
    for c in s:
        if c not in st:
            ans += 2
            st.add(c)
        else:
            ans += 1
    print(ans)

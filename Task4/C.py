n = int(input())
p = list(map(int, input().split()))
total = sum(p)
ans = total
for mask in range(1 << n):
    s = 0
    for i in range(n):
        if mask & (1 << i):
            s += p[i]
    ans = min(ans, abs(total - 2 * s))
print(ans)

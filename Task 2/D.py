t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    common = a[0] if a[0] == a[1] or a[0] == a[2] else a[1]
    for i in range(n):
        if a[i] != common:
            print(i + 1)
            break

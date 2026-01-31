n = int(input())
xs = [int(input()) for _ in range(n)]

m = max(xs)
divs = [0] * (m + 1)

for i in range(1, m + 1):
    for j in range(i, m + 1, i):
        divs[j] += 1

for x in xs:
    print(divs[x])

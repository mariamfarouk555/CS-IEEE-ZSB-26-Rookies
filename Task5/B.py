t = int(input())
for _ in range(t):
    n = int(input())
    a = b = c = -1
    x = n
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            a = i
            x //= i
            break
    if a != -1:
        for j in range(a + 1, int(x ** 0.5) + 1):
            if x % j == 0 and j != a:
                b = j
                c = x // j
                if c != a and c != b and c >= 2:
                    break
                b = -1
    if a != -1 and b != -1 and c != -1:
        print("YES")
        print(a, b, c)
    else:
        print("NO")

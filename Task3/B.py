n, k = input().split()
n = int(n)
k = int(k)
size = 2 * n + 1
r = []
y = []
values = input().split()
for i in range(size):
    r.append(int(values[i]))
    y.append(r[i])
i = 1
while i < 2 * n and k > 0:
    if y[i] > y[i - 1] and y[i] > y[i + 1]:
        if y[i] - 1 > y[i - 1] and y[i] - 1 > y[i + 1]:
            y[i] -= 1
            k -= 1
    i += 2
for val in y:
    print(val, end=" ")

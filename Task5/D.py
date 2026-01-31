import math
X = int(input())
best_a = 1
best_b = X
i = 1
while i * i <= X:
    if X % i == 0:
        a = i
        b = X // i
        if math.gcd(a, b) == 1:
            if max(a, b) < max(best_a, best_b):
                best_a, best_b = a, b
    i += 1
print(best_a, best_b)

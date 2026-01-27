s1 = input().strip()
s2 = input().strip()
target = 0
for c in s1:
    if c == '+':
        target += 1
    else:
        target -= 1
current = 0
q = 0
for c in s2:
    if c == '+':
        current += 1
    elif c == '-':
        current -= 1
    else:
        q += 1
good = 0
total = 1 << q
for mask in range(total):
    pos = current
    for i in range(q):
        if mask & (1 << i):
            pos += 1
        else:
            pos -= 1
    if pos == target:
        good += 1
print(good / total)

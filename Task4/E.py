from itertools import permutations
s = input().strip()
perms = sorted(set(''.join(p) for p in permutations(s)))
print(len(perms))
for p in perms:
    print(p)

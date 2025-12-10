s = input().strip()
if s.isupper() or (s[0].islower() and (len(s) == 1 or s[1:].isupper())):
    print(s.swapcase())
else:
    print(s)

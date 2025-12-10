n = int(input())
s = input().lower()
alphabet = set("abcdefghijklmnopqrstuvwxyz")

if alphabet.issubset(set(s)):
    print("YES")
else:
    print("NO")

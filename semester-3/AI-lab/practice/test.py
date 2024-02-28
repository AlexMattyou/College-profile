p = 'ALEX ALEX'
chars = set(c for w in p for c in w)
print(chars)

w = set()
for c in p:
    if c not in w:
        w.add(c)
print(w)
S = "paraparaparadise"
T = "paragraph"

def ngram(s,n):
    res = []
    for i in range(len(s)-n+1):
        res.append(s[i:i+n])
    return res

X = set(ngram(S,2))
Y = set(ngram(T,2))

wa = X | Y
seki = X & Y
sa1 = X - Y
sa2 = Y - X

print(wa)
print(seki)
print(sa1)
print(sa2)

print("se" in X)
print("se" in Y)


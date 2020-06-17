S = "I am an NLPer"

def ngram(s,n):
    res = []
    for i in range(len(s)-n+1):
        res.append(s[i:i+n])
    return res

ans = ngram(S,2)
print(ans)
T = S.split()
ans = ngram(T,2)
print(ans)

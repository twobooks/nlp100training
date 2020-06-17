import random

S = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def typoglycemia(s):
    res = []
    T = s.split()
    for word in T:
        if len(word)<=4:
            res.append(word)
        else:
            tmp = []
            lis = list(word)
            tmp.append(lis[0])
            tmp += random.sample(lis[1:-1],len(word)-2)
            tmp.append(lis[-1])
            res.append("".join(tmp))
    return res

print(typoglycemia(S))
S = "abcdef"

def cipher(s):
    res = ""
    for c in s:
        if c.islower():
            t = chr(219 - ord(c))
            res += t
        else:
            res += c
    return res

print(cipher(S))
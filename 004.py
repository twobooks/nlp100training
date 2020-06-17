S = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
S = S.split()
S = [""] + S

ans = {}
for i in range(1,len(S)):
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        key = S[i][0]
        ans[key] = i
    else:
        key = S[i][0:2]
        ans[key] = i

print(ans)
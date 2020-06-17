S = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
S = S.replace(".","")
S = S.replace(",","")

ans = list(map(len,S.split()))

print(ans)
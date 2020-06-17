import re

filename = "UK.txt"
with open(filename) as f:
    body = f.read()

regex = re.compile(r"""
(?:ファイル:)
([^(\|\])]*)
""",re.MULTILINE + re.VERBOSE)

res = regex.findall(body)

print(*res,sep="\n")
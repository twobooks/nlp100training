import pandas as pd
import re
import codecs

filename = "UK.txt"
with open(filename) as f:
    body = f.read()

regex = re.compile(r"""
(?P<equals>={2,})
\s*
([^=]*)
\s*
\1
""",re.MULTILINE + re.VERBOSE)

res = regex.findall(body)
ans = {}
for r in res:
    ans[r[1]] = r[0].count("=") - 1

print(*ans.items(),sep="\n")
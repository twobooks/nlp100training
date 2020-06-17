import re
import pickle
import codecs

filename = "UK.txt"
with open(filename,encoding='utf-8') as f:
    body = f.read()

regex = re.compile(r"""
^\{\{基礎情報\s国\n
(.*)
^\}\}\n$
""",re.MULTILINE + re.VERBOSE + re.DOTALL)

body1 = regex.search(body)

regex = re.compile(r"""
\|
([^\s]*)
\s*=\s*
(.*)
""",re.MULTILINE + re.VERBOSE)

res = dict(regex.findall(body1.group(1)))

regex = re.compile(r"""
(\'{2,5})
(.*)
(\1)
""",re.VERBOSE)

for k,v in res.items():
    tmp = re.sub(r"""
        (\'{2,5})
        (.*)
        (\1)
        """,r'\2',v,flags=re.MULTILINE+re.VERBOSE)
    res[k] = tmp

print(*res.items(),sep="\n")

pickle.dump(obj = res,file = open('026.pkl', 'wb'))


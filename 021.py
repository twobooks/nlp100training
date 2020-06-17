import pandas as pd
import re

filename = "jawiki-country.json.gz"
df = pd.read_json(filename,compression='infer',lines=True)

filter = df["title"] == "イギリス"

ans = df[filter].values
body = ans[0][1]

# [[Category:1801年に成立した国家・領域]]
regex = re.compile(r"""
.*
\[\[Category:
.*
""",re.MULTILINE + re.VERBOSE)

ans = regex.findall(body)
print(*ans,sep="\n")
import pandas as pd
import codecs

filename = "jawiki-country.json.gz"
df = pd.read_json(filename,compression='infer',lines=True)

filter = df["title"] == "イギリス"

ans = df[filter].values
ans = ans[0][1]
print(ans)

print(ans,file=codecs.open('UK.txt', 'w', 'utf-8'))

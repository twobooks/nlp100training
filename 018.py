import pandas as pd
import codecs

filename = "popular-names.txt"
df = pd.read_table(filename,header=None,names=["name","sex","count","year"])

sorted_df = df.sort_values("count",ascending=False)
sorted_df.to_csv('018.txt', header=False, index=False, sep='\t', mode='w')

# sort -k 3 -n -r popular-names.txt > 018-2.txt
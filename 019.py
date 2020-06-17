import pandas as pd
import codecs

filename = "popular-names.txt"
df = pd.read_table(filename,header=None,names=["name","sex","count","year"])

unique_df = df["name"].value_counts()
unique_df.to_csv('019.txt', header=False, index=True, sep='\t', mode='w')

# cut -f 1 popular-names.txt > col1.txt
# sort col1.txt | uniq -c | sort -k 1 -n -r > 019-2.txt
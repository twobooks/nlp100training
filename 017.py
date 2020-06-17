import pandas as pd
import codecs

filename = "popular-names.txt"
df = pd.read_table(filename,header=None,names=["name","sex","count","year"])

unique_names = df["name"].unique()
print(*unique_names,sep="\n",file=codecs.open('017.txt', 'w', 'utf-8'))

# cut -f 1 popular-names.txt > col1.txt
# sort col1.txt > 017-2.txt
# uniq 017-2.txt > 017-3.txt
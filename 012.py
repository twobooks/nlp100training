import pandas as pd
import codecs

filename = "popular-names.txt"

df = pd.read_table(filename,header=None,names=["name","sex","count","year"])
print(*df["name"],sep="\n",file=codecs.open('col1.txt', 'w', 'utf-8'))
print(*df["sex"],sep="\n",file=codecs.open('col2.txt', 'w', 'utf-8'))

# cut -f 1 popular-names.txt > col1-2.txt
# cut -f 2 popular-names.txt > col2-2.txt
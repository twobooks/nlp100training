import pandas as pd
import codecs

filename = "col1.txt"
df1 = pd.read_table(filename,header=None,names=["name"])
filename = "col2.txt"
df2 = pd.read_table(filename,header=None,names=["sex"])
df1["sex"] = df2

df1.to_csv('013.txt', header=False, index=False, sep='\t', mode='w')

# paste col1.txt col2.txt > 013-2.txt
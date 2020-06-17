import pandas as pd

filename = "popular-names.txt"

df = pd.read_table(filename,header=None,names=["name","sex","count","year"])
print("行数=",len(df))
print(df.info())

# wc popular-names.txt # linux wc command

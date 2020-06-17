import pandas as pd
import codecs

N = int(input("何分割する？ > "))
filename = input("分割するファイル名を指定 > ")

df = pd.read_table(filename,header=None)

data = len(df)
for i in range(N):
    if i != N-1:
        df[data//N*i:data//N*(i+1)].to_csv(f'016-{i}.txt', header=False, index=False, sep='\t', mode='w')
    else:
        df[data//N*i:].to_csv(f'016-{i}.txt', header=False, index=False, sep='\t', mode='w')

# split -d -n 3 popular-names.txt 016-2-
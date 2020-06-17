import pandas as pd
import codecs

N = int(input("先頭から何行？ > "))
filename = input("ファイル名を指定 > ")

df = pd.read_table(filename,header=None)

print(df[:N])

# head popular-names.txt
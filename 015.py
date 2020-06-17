import pandas as pd
import codecs

N = int(input("末尾から何行？ > "))
filename = input("ファイル名を指定 > ")

df = pd.read_table(filename,header=None)

print(df[-N:])

# tail popular-names.txt
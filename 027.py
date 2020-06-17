import re
import pickle

res = pickle.load(open("026.pkl","rb"))

for k,v in res.items():
    tmp = re.sub(r"""
        \[\[             # '[['(マークアップ開始)
        (?:              # キャプチャ対象外のグループ開始
            [^|]*?       # '|'以外の文字0文字以上、非貪欲
            \|           # '|'
        )*?              # グループ終了、このグループが0か1出現、非貪欲
        (                # グループ開始、キャプチャ対象
          (?!Category:)  # 否定の先読(含んだ場合は対象外としている)
          (.*?)    # '|'以外が0文字以上、非貪欲(表示対象の文字列)
        )
        \]\]        # ']]'（マークアップ終了）
        """, r'\1', v, flags=re.MULTILINE+re.VERBOSE)
    res[k] = tmp

print(*res.items(),sep="\n")

pickle.dump(obj = res,file = open('027.pkl', 'wb'))

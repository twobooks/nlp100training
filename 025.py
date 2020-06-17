import re

filename = "UK.txt"
with open(filename) as f:
    body = f.read()

regex = re.compile(r"""
^\{\{基礎情報\s国\n
(.*)
^\}\}\n$
""",re.MULTILINE + re.VERBOSE + re.DOTALL)

body1 = regex.search(body)

# |公式国名 = {{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br />
# *{{lang|gd|An Rìoghachd Aonaichte na Breatainn Mhòr agus Eirinn mu Thuath}}（[[スコットランド・ゲール語]]）
# *{{lang|cy|Teyrnas Gyfunol Prydain Fawr a Gogledd Iwerddon}}（[[ウェールズ語]]）
# *{{lang|ga|Ríocht Aontaithe na Breataine Móire agus Tuaisceart na hÉireann}}（[[アイルランド語]]）
# *{{lang|kw|An Rywvaneth Unys a Vreten Veur hag Iwerdhon Glédh}}（[[コーンウォール語]]）
# *{{lang|sco|Unitit Kinrick o Great Breetain an Northren Ireland}}（[[スコットランド語]]）
# **{{lang|sco|Claught Kängrick o Docht Brätain an Norlin Airlann}}、{{lang|sco|Unitet Kängdom o Great Brittain an Norlin Airlann}}（アルスター・スコットランド語）</ref>

regex = re.compile(r"""
\|
([^\s]*)
\s*=\s*
(.*)
""",re.MULTILINE + re.VERBOSE)

ans = dict(regex.findall(body1.group(1)))
print(*ans.items(),sep="\n")
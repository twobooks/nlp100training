# with open("popular-names.txt", "r") as f:
#     ans = []
#     for data in f:
#         ans.append(data.strip().replace("\t"," "))
# print(ans[:5])

import re
import codecs

with open('popular-names.txt', 'r') as file:
    text = re.sub('\t', ' ', file.read())
    print(text, file=codecs.open('011test.txt', 'w', 'utf-8'))

# sed -e 's/\t/ /g' popular-names.txt > sedtest.txt
# tr '\t' ' ' < popular-names.txt > trtest.txt
# expand --tabs=1 popular-names.txt > expandtest.txt
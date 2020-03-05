import MeCab
import collections
import pprint
import re
import csv

mecab = MeCab.Tagger('/usr/local/lib/mecab/dic/mecab-ipadic-neologd')



with open('/Users/mayu/Git/PythonNLP/data/kusamakura.txt') as f:
    text=f.read()
text = re.sub("\n","",text)
text = re.sub("\r","",text)
text = re.sub("\u3000","",text)
while(1):
    t = '※' in text
    if t == False:
        break
    m = re.search(r'※',text)
    n = re.search(r'\)',text)
    p = m.start()
    q = n.end()

    a = text[:p]
    b = text[q:]

    text = a+b

mecab.parse('')
node = mecab.parseToNode(text)
m = {}
while node:
    
    word = node.surface
    pos = node.feature.split(",")[0]
    if pos =="名詞":
        if(word in m):
            m[word] += 1
        else:
            m[word] = 1
    
    node = node.next

n=sorted(m.items(),key=lambda x:x[1],reverse=True)
#pprint.pprint(n)



with open('/Users/mayu/Git/PythonNLP/mayu/result.csv','w') as g:
    writer = csv.writer(g)
    writer.writerows(n)
    
   
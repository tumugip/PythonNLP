import re

l = 0

with open('/Users/mayu/Git/PythonNLP/data/kusamakura.txt') as f:
    text=f.read()
with open('/Users/mayu/Git/PythonNLP/data/kusamakura.txt') as f:
    for line in f:
        l +=1
print("line:",l)
word = len(text)
print("words:",word)
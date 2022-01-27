with open("top10000words.txt", 'r') as f:
    allwords = f.readlines()
fiveletterwords = []
for word in allwords:
    if len(list(word)) == 6:
        fiveletterwords.append(word.lower())

with open('5lettertop10k.txt', 'w') as g:
    g.writelines(fiveletterwords)
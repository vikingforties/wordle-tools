print("Format is fghjstei:t:____n")
print("Letters to ignore : Letters to include (yellow) : Letters correctly placed (green)")
clue = input("What's the clue? ").split(':')
#clue = "arosearose::_____".split(':')
ignore = clue[0]
use = clue[1]
placed = clue[2]
print(ignore, use, placed, "  criteria letters.")

with open("5letterwords.txt", 'r') as f:
    words = f.readlines()
print(len(words), " total words.")

if ignore:
    removes = []
    ignorelist = list(ignore)
    for word in words:
        for letter in ignorelist:
            if letter in word:
                removes.append(word)
    removeset = set(removes)
    remaining = [i for i in words if i not in removeset]   
    words = remaining
    print(len(words), "  words after ignoring letters.")      

if use:
    uselist = list(use)
    usesletters = []
    for word in words:
        lettercount = 0
        for letter in uselist:
            if letter in word:
                lettercount += 1
        if lettercount == len(uselist):
            usesletters.append(word)
    words = usesletters
    #print(words)

if placed:
    placedlist = list(placed)
    gotplaced = []
    justtheletters = [i for i in placedlist if i != '_']
    for word in words:
        wordlist = list(word)
        lettercount = 0
        for i, letter in enumerate(placedlist):
            if letter == '_':
                next
            elif letter == wordlist[i]:
                lettercount += 1
        #print(lettercount)
        if lettercount == len(justtheletters):
            gotplaced.append(word)
    words = gotplaced

orderedwords = []
with open("5lettertop10k.txt", 'r') as f:
    mostcommon = f.readlines()
for commonword in mostcommon:
    if commonword in words:
        orderedwords.append(commonword)

uncommonwords = []
for word in words:
    if word not in mostcommon:
        uncommonwords.append(word)

words = orderedwords + uncommonwords

for word in words:
    print(word)

print(len(words), " candidates.")
print(':'.join(clue), "  last used letters.")
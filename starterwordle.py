with open("5letterscrabble.txt", 'r') as f:
    allwords = f.read()
allletters = list(allwords)
print(len(allletters))
allletters.sort()

alphabet = "abcdefghijklmnopqrstuvwxyz"
counts = {}
for each in list(alphabet):
    #print(allletters.count(each))
    counts[each] = allletters.count(each)

counts2 = dict(sorted(counts.items(), reverse=True , key= lambda X:X[1]))
for key, val in counts2.items():
    print(key, ':', val)

# top scoring letter word from 5letterwords, 5lettertop10k & 5letterscrabble: arose
'''
Also: arles, earls, lares, laser, lears, rales, reals, seral, 
aster, rates, resat, stare, tares, tears
Most vowels:  adieu

2nd starter words if first blank with remaining vowels: until, build, built, input, fluid, unity, guild
more consonants: think, night, light, might, child, thing
'''
with open("5lettertop10k.txt", 'r') as f:
    words = f.readlines()

vowels = list('aeiou')
vowelmatrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

for x, vowel in enumerate(vowels):
    for word in words:
        word.strip()
        letters = list(word)
        for i, letter in enumerate(letters):
            if vowel == letter:
                vowelmatrix[x][i] += 1

print("Letter Placings:")
print("   1st 2nd  3rd 4th 5th")
for row, vowel in zip(vowelmatrix, vowels):
    print(vowel, row)
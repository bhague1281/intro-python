word = raw_input("Enter a word: ")

letters = {}

for l in word:
  if l in letters:
    letters[l] = letters[l] + 1
  else:
    letters[l] = 1

for key in letters:
  print '{} : {}'.format(key, letters[key])

# print letters
# ask the user for a word and print the length of the word.
# exit when the user types 'EXIT', and print 'Done!' when finished

while True:
  word = raw_input("Enter a word (type EXIT to quit): ")
  if word == 'EXIT':
    break
  print len(word)

print "Done!"
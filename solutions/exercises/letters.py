# word = raw_input('Enter a word: ')
# while word.lower() != 'exit':
#     print len(word)
#     word = raw_input('Enter a word: ')
#
# print('Goodbye!')

word = ''
while True:
    word = raw_input('Enter a word: ')
    if word.lower() == 'exit':
        break
    print len(word)

print('Goodbye!')

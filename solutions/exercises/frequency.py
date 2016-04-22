sentence = ''
while True:
    sentence = raw_input('Enter a sentence: ')
    if sentence.lower() == 'exit':
        break
    # do something here
    frequency = {}
    for char in sentence:
        if char in frequency:
            frequency[char] += 1
            # frequency[char] = frequency[char] + 1
        else:
            frequency[char] = 1
    print frequency

print('Goodbye!')

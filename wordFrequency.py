def word_frequency(word):
    
    if word[-1] == '.':
        word = word[0:len(word) - 1]

    if word in dictionary:
        dictionary[word] +=  1

    else:
        dictionary.update({word: 1})
    
    dictionary = {}

    sentence = "This is a test sentence. This sentence is a test."
	# calling the function
    lst = sentence.split()

    for word in lst:
        word_frequency(word)

    for keys in dictionary:
        print(keys)
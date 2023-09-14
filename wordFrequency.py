dictionary = {}
def word_frequency(word):
    
    if word[-1] == '.':
        word = word[0:len(word) - 1]

    if word in dictionary:
        dictionary[word] +=  1

    else:
        dictionary.update({word: 1})

    for keys in dictionary:
        print (keys, end = " ")
        print (":", end = " ")
        print (dictionary[keys], end = " ")
        print()
    
    
if __name__ == "__main__":
    sentence = "This is a test sentence. This sentence is a test."
	# calling the function
    lst = sentence.split()

    for word in lst:
        word_frequency(word)

    
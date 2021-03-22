vowels__= ["a", "i","e","o","u"]
word1="Military"
word2="eerchanaummiiii"

# using set
def unique_set(wordset, vowelset):
    set_1 = set()
    for letter1 in wordset:
        if letter1 in vowelset:
            set_1.add(letter1)
    return set_1

print(unique_set(word2,vowels__))

def unique_list(word, vowels):
    """
    Takes a string and list of vowels and outputs a list of unique vowels found in the input string
    :param word:
    :param vowels:
    :return:
    """
    output_list = []
    for letter in word:
        if letter not in output_list:
            if letter in vowels:
                output_list.append(letter)
    return output_list


vowels_found = unique_list(word1, vowels__)
print(len(vowels_found))



#print(unique(word2, vowels))




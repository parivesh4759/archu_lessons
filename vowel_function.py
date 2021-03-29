def search_vowel(word):
    """Hi..this is ur vowel search function"""
    vowels = set('aeiou')
    vowels_found_in_word = vowels.intersection(set(word))
    for i in vowels_found_in_word:
        print(i)


user_word = input("hi user enter a word:")
search_vowel(user_word)

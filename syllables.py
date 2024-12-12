import re
def counter(word):
    '''
    Count the number of syllables in a word.
    :param word: the word to count syllables for
    :return: int: the number of syllables in a word
    '''

    # make sure it is a string
    if isinstance(word, str):
        # make lowercase
        word = word.lower()
    else:
        word = str(word).lower()

    # if word is less than three letters it is one syllable
    if len(word) <= 3:
        return 1
    # remove silent e at end and es
    word = re.sub('(?:[^laeiouy]es|[^laeiouy]e)$', '', word)

    #count vowels for syllables including clusters of 2+
    vowel_count = re.findall('[aeiouy]+', word)

    return len(vowel_count)

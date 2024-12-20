import syllables
import nltk
import nltk.tokenize

nltk.download('punkt_tab')

# for this I need a list of words from the text
# total syllables
# avg syllables per word

def sentence_list(text):
    '''
    returns a list of sentences in a text
    :param text: the text to be tokenized
    :return: a list of sentences
    '''
    #split the text into sentences:
    sentences = nltk.tokenize.sent_tokenize(text)
    return sentences

def word_list(text):
    '''
    returns a list of words in a text removing punctuation
    :param text: the text to be tokenized
    :return: a list of words
    '''
    tokens = nltk.tokenize.word_tokenize(text)
    #remove punctuation
    tokens = [token for token in tokens if token.isalnum()]
    return tokens

def sentence_counter(text):
    '''
    Counts the number of sentences in a given text.
    :param text: the text to be analyzed
    :return: int, the number of sentences
    '''
    return len(sentence_list(text))

def word_counter(text):
    '''
    Counts the number of words in a given text.
    :param text: the text to be analyzed
    :return: int, the number of words
    '''
    return len(word_list(text))

def avg_sent_length(text):
    '''
    Counts the average sentence length in a given text.
    :param text: the text to be analyzed
    :return: int, the average sentence length
    '''
    total_words = word_counter(text)
    total_sentences = sentence_counter(text)
    return total_words / total_sentences

def syllable_count(text):
    '''
    Counts the number of syllables in a given text.
    :param text: the text to be analyzed
    :return: int, the number of syllables
    '''
    # return list of tokens
    tokens = word_list(text)
    #remove punctuation
    syllable_list = [syllables.counter(token) for token in tokens]
    return sum(syllable_list)

def avg_syllable_per_word(text):
    '''
    Counts the average syllables per word in a given text.
    :param text: the text to be analyzed
    :return: int, the average syllables per word
    '''
    return syllable_count(text) / word_counter(text)

def kf_score(text):
    '''
    Computes the Flesch-Kincaid score of a given text
    :param avg_sent_len: the average length of sentences in the text
    :param avg_syll_per_word: the average number of syllables per word in the text
    :return: the Flesch-Kincaid score
    '''
    avg_syll = avg_syllable_per_word(text)
    avg_sent_len = avg_sent_length(text)
    return (.38*avg_sent_len+11.8*avg_syll)-15.59
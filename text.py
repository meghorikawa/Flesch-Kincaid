import syllables
import nltk.tokenize
import re
from nltk.tokenize import sent_tokenize, word_tokenize


# for this I need a list of words from the text
# total syllables
# avg syllables per word

def sentence_counter(text):
    '''
    Counts the number of sentences in a given text.
    :param text: the text to be analyzed
    :return: int, the number of sentences
    '''
    #split the text into sentences:
    sentences = nltk.tokenize.sent_tokenize(text)
    return len(sentences)


def word_counter(text):
    '''
    Counts the number of words in a given text.
    :param text: the text to be analyzed
    :return: int, the number of words
    '''
    tokens = nltk.tokenize.word_tokenize(text)
    #remove punctuation
    tokens = [token for token in tokens if token.isalnum()]
    return len(tokens)


def avg_sent_length(text):
    '''
    Counts the average sentence length in a given text.
    :param text: the text to be analyzed
    :return: int, the average sentence length
    '''
    total_words = word_counter(text)
    total_sentences = sentence_counter(text)
    return total_words / total_sentences



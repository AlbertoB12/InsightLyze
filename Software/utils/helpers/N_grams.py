"""
# Help-utility to create uni, bi and trigrams of a dataset with tweets
"""

### Packages
import nltk
from nltk.util import ngrams
from collections import Counter

### Functions
# Function to create uni, bi and trigrams of a dataset with tweets
# Gets list of strings (tweets)
# Returns dictionary with uni, bi and trigrams
def n_grams(input):
    one = [] #Unigrams - most frequent words
    two = [] #Bigrams
    three = [] #Trigrams
    for text in input: #Open all tweets, one by one
        tokens = nltk.word_tokenize(text.lower()) #Tokenize tweet
        # Unigrams
        for token in tokens:
            one.append(token) #Save all tokens in list 'one'
        # Bigrams
        bi = ngrams(tokens, 2)
        for gram in bi:
            two.append(gram)
        # Trigrams
        tri = ngrams(tokens, 3)
        for gram in tri:
            three.append(gram)
    # Count number of uni, bi and trigrams to be used for the statistics
    unigrams = Counter(one)
    bigrams = Counter(two)
    trigrams = Counter(three)
    return unigrams, bigrams, trigrams
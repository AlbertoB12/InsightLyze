"""
# Help-utility to untokenize tweets
"""

### Packages
import nltk

### Functions
# Main function to untokenize tweets
# Gets list of lists with strings
# Returns list with strings (cleaned tweets)
def untokenize(corpus):
    sentences_untokenized = []
    for tokens in corpus:
        tweet = nltk.tokenize.treebank.TreebankWordDetokenizer().detokenize(tokens)
        sentences_untokenized.append(tweet)
    return sentences_untokenized
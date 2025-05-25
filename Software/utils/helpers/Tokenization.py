"""
# Help-utility to tokenize tweets
"""

### Packages
import nltk

### Functions
# Main function to tokenize tweets
# Gets a list of strings
# Returns a list of lists with strings (tokens)
def tokenization(corpus):
    nltk.download('punkt_tab', quiet=True) #Download needed ressources (if needed)
    tokens = []
    for tweet in corpus:
        tokenization = nltk.word_tokenize(tweet, "english")
        tokens.append(tokenization)
    return tokens
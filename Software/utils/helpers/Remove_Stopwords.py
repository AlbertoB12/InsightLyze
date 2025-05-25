"""
# Help-utility to remove stopwords from tweets
"""

### Packages
import nltk

### Functions
# Main Function to remove stopwords from tweets
# Gets list of lists with strings (lemmas)
# Returns list of lists with strings (lemmas without stopwords)
def remove_stopwords(corpus):
    filtered_tokens = []
    stopwords = set(nltk.corpus.stopwords.words("english"))
    for lines in corpus:
        tokens_no_stopwords = []
        for token in lines:
            if token not in stopwords:
                tokens_no_stopwords.append(token)
        filtered_tokens.append(tokens_no_stopwords)
    return filtered_tokens
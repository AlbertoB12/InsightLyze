"""
# Help-utility to lemmatize tweets
"""

### Packages
from nltk.stem import WordNetLemmatizer

### Functions
# Main function to lemmatize tokens
# Gets list of list with strings (tokens)
# Returns list of list with strings (lemmas)
def lemmatization(tokens):
    tokens_lemma = []
    lemmatizer = WordNetLemmatizer()
    for lines in tokens:
        tokens_lemmatized = []
        for token in lines:
            lemma = lemmatizer.lemmatize(token)
            tokens_lemmatized.append(lemma)
        tokens_lemma.append(tokens_lemmatized)
    return tokens_lemma
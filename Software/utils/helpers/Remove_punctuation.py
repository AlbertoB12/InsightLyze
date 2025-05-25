"""
# Help-utility to remove punctuation from tweets
"""

### Packages
import re
import string

### Functions
# Main function to remove punctuation from tweets
# Receives a list of strings
# Returns a list of strings (tweets with no punctuation)
def remove_punctuation(corpus):
    tweets_no_punctuation = []
    punctuation_pattern = re.compile(r"[" + re.escape(string.punctuation) + "]")
    for tweet in corpus:
        new_tweet = punctuation_pattern.sub(r'', tweet)
        tweets_no_punctuation.append(new_tweet)
    return tweets_no_punctuation
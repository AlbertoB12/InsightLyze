"""
# Help-utility to lower case all tweets in a dataset
"""

### Functions
# Main function to lower case all texts in a dataset
# Gets a list of strings
# Returns list with lower cased tweets
def lower_case(corpus):
    tweets_low = []
    for tweet in corpus:
        tweet_lower = tweet.lower()
        tweets_low.append(tweet_lower)
    return tweets_low
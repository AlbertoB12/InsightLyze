"""
# Help-utility to remove pipes from strings
"""

### Packages
import re

### Functions
# Main function to remove pipes from strings
# Takes a list of strings
# Returns a list of strings with pipes removed
def remove_pipes(corpus):
    tweets_no_pipes = []
    # Use regex to match pipes
    pipe_pattern = re.compile(r'\|')
    for tweet in corpus:
        tweet_no_pipes = pipe_pattern.sub(r'', tweet)
        tweets_no_pipes.append(tweet_no_pipes)
    return tweets_no_pipes
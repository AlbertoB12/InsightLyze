"""
# Help-utility to remove usernames from tweets
"""

### Packages
import re

### Functions
# Main function to remove usernames from tweets
# Takes a list of strings
# Returns a list of strings with tweets without usernames
def remove_usernames(corpus):
    tweets_no_usernames = []
    # Use regex
    username_pattern = re.compile(r'@([A-Za-z0-9_]+)')
    for tweet in corpus:
        new_tweet = username_pattern.sub(r'', tweet)
        tweets_no_usernames.append(new_tweet)
    return tweets_no_usernames
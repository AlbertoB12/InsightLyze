"""
# Help-utility to remove URLs from tweets
"""

### Packages
import re

### Functions
# Function to remove all URLs from tweets
# Takes list of strings (tweets)
# Returns list of tweets with no URLs
def remove_URLs(corpus):
    tweets_no_url = []
    # Use regex
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    for tweet in corpus:
        tweets_no_URLs = url_pattern.sub(r'', tweet)
        tweets_no_url.append(tweets_no_URLs)
    return tweets_no_url
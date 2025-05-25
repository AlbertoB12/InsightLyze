"""
# Help-utility to remove hash from tweets
"""

### Packages
# No imports needed

### Functions
# Main function to remove hash from tweets
# Receives a list of strings
# Returns a list of strings (tweets with no hash)
def remove_hash(input):
    tweets_no_hash = []
    for tweet in input:
        cleaned_text = tweet.replace('#', '')
        tweets_no_hash.append(cleaned_text)
    return tweets_no_hash
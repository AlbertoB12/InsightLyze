"""
# Utility to scrape tweets
# The Search_tweets.search() of this utility will work if user has a valid X-key for scraping the social network
"""

### Packages
from utils.helpers import Save_directory, Query_creation, Search_tweets, Save_tweets

### Functions
# Main function to set directory, create query and search and save tweets
def scrape():
    # Let user decide and create the directory to save tweets
    directory = Save_directory.save()
    # Create query
    query = Query_creation.query_creation()
    # Search for tweets
    tweets = Search_tweets.search(query) #It will work if user has a valid X-key for scraping the social network
    # Save tweets
    Save_tweets.save_tweets(tweets, directory)
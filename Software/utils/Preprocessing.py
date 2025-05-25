"""
# Utility to preprocess and save tweets
# Tweets are cleaned
# Afterwards, clean tweets are saved in new directory
"""

### Packages
from utils.helpers import config, Remove_URLs, Remove_usernames, Remove_pipes, Save_tweets
from utils import Show_message
import os

### Fuctions
# Main function to preprocess tweets and save them in the selected path in a new .csv file
# Gets list of strings
def preprocess_and_save(corpus):
    # Preprocessing
    clean_tweets = preprocessing(corpus)
    # Save tweets
    # Create new directory
    path = os.path.join(config.GLOBAL_VARIABLE_SEARCH_TWEETS_PATH, "clean")
    # Create the directory
    os.makedirs(path, exist_ok=True) #Use os.makedirs to avoid errors if the directory already exists
    # Save save_path as global variable
    config.GLOBAL_VARIABLE_CLEAN_TWEETS_PATH = path
    Show_message.show_message(f"Saving cleaned tweets to path: {config.GLOBAL_VARIABLE_CLEAN_TWEETS_PATH}", "Saving")
    Save_tweets.save_tweets(clean_tweets, config.GLOBAL_VARIABLE_CLEAN_TWEETS_PATH) #Save tweets
    Show_message.show_message("Tweets saved", "Saved")

# Function to eliminate from all the tweets: URLs and usernames
# The result are cleaned tweets, which can, after that, be correctly analyzed applying NLP methods.
# Takes list of stings (tweets)
# Returns list of strings (clean tweets)
def preprocessing(corpus):
    Show_message.show_message("Preprocessing tweets", "Preprocessing")
    # 1nd: Remove URLs
    tweets_no_URLs = Remove_URLs.remove_URLs(corpus)
    # 2rd: Remove usernames
    tweets_no_usernames = Remove_usernames.remove_usernames(tweets_no_URLs)
    Show_message.show_message("Tweets preprocessed", "Preprocessed")
    # 3rd: Remove pipes ("|")
    tweets_no_pipes = Remove_pipes.remove_pipes(tweets_no_usernames) #In order to have no problems with the delimiter
                                                                     # (sep) while saving classificated tweets
    return tweets_no_pipes
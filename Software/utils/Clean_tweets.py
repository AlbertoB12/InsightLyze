"""
# Utility to clean tweets for making statistics from them
"""

### Packages
from utils.helpers import config, Lower_case, Remove_punctuation, Tokenization, Lemmatization, Remove_Stopwords, \
    Untokenize, Save_tweets, Remove_hash
from utils import Show_message, Read_csv
import os

### Functions
# Main function to clean tweets for making statistics from them and saving them afterwards
# Gets path
# Saves new path where new tweets are
# Returns list of strings (tweets)
def clean_and_save_tweets(path):
    Show_message.show_message("Starting the cleaning process for statistics", "Cleaning")
    # Open tweets
    tweets, classifications = open(path)
    # Clean tweets
    final_tweets = clean_tweets(tweets)
    # Create new list to be saved with clean tweets and classifications
    final_list = merge_lists(final_tweets, classifications)
    # Create new folder for saving this tweets and save them
    new_path = os.path.join(path, "statistics")
    os.makedirs(new_path, exist_ok=True) #Use os.makedirs to avoid errors if the directory already exists
    config.GLOBAL_VARIABLE_CLEAN_TWEETS_PATH2 = new_path #Save new path
    # Save new cleaned tweets
    Save_tweets.save_tweets(final_list, new_path)
    Show_message.show_message("Cleaning process finalized", "Done")

# Function to clean tweets for making statistics from them
# Gets list of strings
# Returns list of strings
def clean_tweets(tweets):
    # 1st: Lowercase
    tweets_low = Lower_case.lower_case(tweets)
    # 2nd: Remove punctuation
    tweets_no_punctuation = Remove_punctuation.remove_punctuation(tweets_low)
    # 3rd: Remove #
    tweets_no_hash = Remove_hash.remove_hash(tweets_no_punctuation)
    # 4th: Tokenization
    tokens = Tokenization.tokenization(tweets_no_hash)
    # 5th: Lemmatization
    lemmas = Lemmatization.lemmatization(tokens)
    # 6th: Remove stopwords
    lemmas_no_stopwords = Remove_Stopwords.remove_stopwords(lemmas)
    # 7th: Untokenize (create sentences again)
    tweets_final = Untokenize.untokenize(lemmas_no_stopwords)
    return tweets_final

# Function to open file with tweets and classifications
# Gets path
# Returns 2 lists of strings, one with tweets and one with classifications
def open(path):
    tweets = Read_csv.read_csv(path) #Read file in directory and get list of strings (tweets to be analysed)
    # Keep first part and rest separately
    before_pipe = [] #List to store the parts before the first "|"
    after_pipe = [] #List to store the parts after the first "|", including the pipe
    for line in tweets:
        if '|' in line:
            first_part, remaining_part = line.split('|', 1) #Split only at the first "|"
            before_pipe.append(first_part) #Append the part before "|"
            after_pipe.append('|' + remaining_part) #Append the "|" + remaining part
    return before_pipe, after_pipe

# Function to merge lists with tweets and classifications
# Gets 2 lists of strings, one with clean tweets and one with classifications
# Returns merged list, a list of strings (with tweets and classifications together)
def merge_lists(list1, list2):
    merged = []
    for part1, part2 in zip(list1, list2):
        merged.append(part1 + part2) #Concatenate corresponding strings
    return merged
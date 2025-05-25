"""
###InsightLyze, the social media analysis tool###
                ### VERSION: 1.0 ###

# Main script of the program to run the software
# 1st: Check and install pip and all necessary packages to run the software
# 2nd: Scrape tweets (save directory, define search query, search for tweets and save tweets)
# 3rd: Preprocess tweets (clean) and save tweets
# 4th: Classify tweets (sentiment, emotion, topic)
# 5th: Create statistics (n_grams, wordcloud and classifications)
# The software guides the user throughout all the process
"""

### Packages
from utils import Show_message, Check_and_install_packages, Scrape, Preprocessing, Read_csv, Classification, Statistics,\
    Clean_tweets
from utils.helpers import config

### Run software
if __name__ == "__main__":
    # Welcome message
    Show_message.show_message("Welcome to InsightLyze, the social media analysis tool.\nPlease follow the instructions",
                              "Welcome")
    # Check and install pip and all needed packages and version
    Check_and_install_packages.check_and_install()
    # Scrape process: Set save directory, create search query and search and save tweets
    Scrape.scrape()
    # Preprocess and save the clean tweets to analyse them later (remove URLs, usernames and pipes ('|'))
    tweets = Read_csv.read_csv(config.GLOBAL_VARIABLE_SEARCH_TWEETS_PATH) #Import first .csv file with tweets
    Preprocessing.preprocess_and_save(tweets)
    # Classification (analyse sentiment, emotion and topic of tweets)
    Classification.classification(config.GLOBAL_VARIABLE_CLEAN_TWEETS_PATH)
    # Clean tweets to make statistics afterwards (lowercase, remove punctuation and stopwords, tokenize and lemmatize)
    Clean_tweets.clean_and_save_tweets(config.GLOBAL_VARIABLE_CLEAN_TWEETS_PATH)
    # Statistics (n_grams (uni, bi and trigrams), wordcloud and classification)
    Statistics.statistics(config.GLOBAL_VARIABLE_CLEAN_TWEETS_PATH2)
    # Finish message
    Show_message.show_message("Process finalized", "Done")

                                              ### End of software ###
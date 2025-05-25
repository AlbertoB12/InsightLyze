"""
# Utility to create statistics (n_grams, wordcloud and classifications (sentiment, emotion and topics)) from tweets
"""

### Packages
import pandas as pd
import os
from utils.helpers import N_grams, Save_ngrams, Wordcloud, Save_classifications
from utils import Show_message

### Functions
# Main function to create statistics (n_grams, wordclouds and classifications (sentiment, emotion and topics)) from tweets
# Gets path to actual folder
def statistics(input):
    Show_message.show_message("Starting statistics", "Statistics")
    # Open file with tweets and classifications
    df = pd.read_csv(os.path.join(input, "Tweets.csv"), sep='|', encoding="latin-1", header=None) #Read file and save it
                                                                                                  #as pandas df
    # Create uni, bi and trigrams
    Show_message.show_message("Creating n_grams", "n_grams")
    unigrams, bigrams, trigrams = N_grams.n_grams(df[0].tolist()) #Give function column of the df with tweets (1st column)
    Save_ngrams.save_ngrams(input, unigrams, bigrams, trigrams) #Save n_grams
    Show_message.show_message("n_grams created", "Done")
    # Create wordcloud
    Show_message.show_message("Creating Wordcloud from unigrams", "Wordcloud")
    Wordcloud.wordcloud(input, unigrams)
    Show_message.show_message("Wordcloud created", "Done")
    # Create statistics of classifications
    Show_message.show_message("Creating classifications", "Classifications")
    Save_classifications.save_classifications(input, df)
    Show_message.show_message("Classifications created", "Done")
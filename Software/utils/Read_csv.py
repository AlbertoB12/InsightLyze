"""
# Utility to read .csv files and return tweets
"""

### Packages
import csv, os

### Functions
# Function to open .csv file in a directory
# Gets directory
# Returns tweets
def read_csv(directory):
    tweets = []  #Empty list to be returned with tweets
    file_path = os.path.join(directory, "Tweets.csv")
    with open(file_path, 'r', encoding='utf-8-sig', errors="ignore") as file: #Use utf-8-sig to handle BOM
        csv_reader = csv.reader(file, delimiter="\n")
        for row in csv_reader:
            #Check if the row is not empty and contains a non-empty string
            if row and row[0].strip():
                tweets.append(row[0].strip()) #Strip any extra whitespace
    return tweets
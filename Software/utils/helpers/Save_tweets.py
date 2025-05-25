"""
# Help-utility to save scraped tweets
"""

### Packages
import csv
import tkinter as tk
from tkinter import messagebox

### Functions
# Main function to save scraped tweets in the elected path
# It creates a CSV file
# User gets success or error messages in an opening window
# Gets list of strings (tweets) and path
def save_tweets(tweets, save_path):
    # Initialize the tkinter root window
    root = tk.Tk()
    root.withdraw() #Hide the root window
    # If the list of tweets is not empty, process it
    if len(tweets) != 0:
        # Write .csv
        messagebox.showinfo("Saving", "Saving tweets.")
        with open(f'{save_path}/Tweets.csv', 'a', encoding="UTF-8", newline="") as file:
            # Initialize the CSV writer
            csv_writer = csv.writer(file)
            # Save each tweet as a row
            for tweet in tweets:
                csv_writer.writerow([tweet.replace("\n", " ")])
            # Show success message
            messagebox.showinfo("Success", f"File successfully created and saved in {save_path}.")
    else:
        # Show error message
        messagebox.showwarning("No Tweets", "No tweets found.")
    # Close the tkinter root window
    root.destroy()
"""
# Help-utility to search for tweets using a query
# It opens a window for user to introduce the desired label and search dates
"""

### Packages
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import tweepy, ssl
from utils.helpers import Authetication_keys

### Functions
# Main function to search for tweets with a query, label, desired number of results and dates
# Gets X-client, label and query (strings), int (max. results) and from_date and to_date (strings)
# Returns list of strings (scraped tweets)
def search_tweets(client, label, query, max_results, from_date, to_date):
    tweets = [] #Empty list to save all scraped tweets
    for tweet in client.search_all_tweets( #Search from whole X archive
        label=label,
        query=query,
        maxResults=max_results,
        fromDate=from_date,
        toDate=to_date
    ):
        tweets.append(tweet)
    return tweets

# Function for preparations
# Disable SSL certificate and authenticate with X API
# Returns X-client
def preparation():
    # Disable SSL certificate verification to allow HTTPS connections to servers with self-signed or untrusted certificates.
    ssl._create_default_https_context = ssl._create_unverified_context
    # Manage authentication keys
    keys = Authetication_keys.manage_keys()
    # Authentication with X
    auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
    auth.set_access_token(keys['access_token'], keys['access_token_secret'])
    client = tweepy.Client(keys['bearer_token'])
    api = tweepy.API(auth, wait_on_rate_limit=True) #At the moment not used
    return client

# Function to get user's input and perform tweet search
# It opens a window for user to decide label and dates
# Gets string (query)
# Returns list of strings (tweets)
def search(query):
    # Prepare and authenticate
    client = preparation()
    global tweets_list
    tweets_list = []
    # Window with submit process
    def submit():
        global tweets_list
        label = label_entry.get() #Introduce label
        try:
            max_results = int(results_entry.get()) #Introduce desired max. number of results
        except ValueError: #If error
            messagebox.showwarning("Input Error", "Please enter a valid number for results.")
            return
        # Introduce dates to search for tweets
        # Select them from a calendar
        from_date = from_date_entry.get_date().strftime("%Y%m%d%H%M")
        to_date = to_date_entry.get_date().strftime("%Y%m%d%H%M")
        # If something is missing
        if not label:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return
        # Perform the search
        tweets = search_tweets(client, label, query, max_results, from_date, to_date)
        tweets_list = tweets
        messagebox.showinfo("Search Completed", f"Found {len(tweets)} tweets.")
        root.destroy()  # Close the window
    # Initialize tkinter window
    root = tk.Tk()
    root.title("Twitter Search Query Generator")
    # Create UI components
    tk.Label(root, text="Label:").pack(pady=5)
    label_entry = tk.Entry(root, width=50)
    label_entry.pack(pady=5)
    tk.Label(root, text="Number of Results:").pack(pady=5)
    results_entry = tk.Entry(root, width=50)
    results_entry.pack(pady=5)
    tk.Label(root, text="From Date:").pack(pady=5)
    from_date_entry = DateEntry(root, width=50, background='darkblue', foreground='white', borderwidth=2)
    from_date_entry.pack(pady=5)
    tk.Label(root, text="To Date:").pack(pady=5)
    to_date_entry = DateEntry(root, width=50, background='darkblue', foreground='white', borderwidth=2)
    to_date_entry.pack(pady=5)
    tk.Button(root, text="Submit", command=submit).pack(pady=20)
    root.mainloop()
    return tweets_list
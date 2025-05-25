"""
# Help-utility to create a suitable X search query from the input of the user
# Program opens a window to facilitate the process
# If no input is given, program waits
# User has to give one or more words of the term he wants to search for
# Returns the search query
"""

### Packages
import nltk, string, sys, os
from nltk.corpus import stopwords
from tkinter import Tk, Label, Entry, Button, messagebox

### Functions
# Main function to call both functions (search and query processing) and create the query
# Returns string (query)
def query_creation():
    query = get_search()
    return query

# Function to get what user wants to search for
# Returns string
def get_search():
    # Initialize tkinter window for better user interface
    root = Tk()
    root.title("X Search Query Generator")
    # Create a label and text entry for user input
    Label(root, text="Enter the term(s) you want to search for on X:").pack(pady=10)
    query_entry = Entry(root, width=50)
    query_entry.pack(padx=20, pady=10)
    # Function to be called when the user clicks the "Submit" button
    def on_submit():
        user_input = query_entry.get()
        if user_input.strip() == "": #If input is empty
            messagebox.showwarning("Input Error", "Please enter a search query.")
        else: #If input is not empty
            # Generate search query
            search_query = query_processing(user_input)
            messagebox.showinfo("Generated Query", f"Your X search query is:\n\n{search_query}")
            root.quit() #Close the window
            root.search_query = search_query #Save the search query in the root window
    # Submit button
    Button(root, text="Submit", command=on_submit).pack(pady=20)
    root.mainloop() #Start the tkinter event loop
    return root.search_query #Return the generated search query

# Function to process the obtained input of search keywords to a more suitable search query
# Gets string
# Returns string
def query_processing(input):
    query_processed = ""
    # Eliminate punctuation if existing
    input_clean = input.translate(str.maketrans('', '', string.punctuation))
    if len(input_clean.split()) > 1: #If there is more than one word
        # Set NLTK data path and download stopwords if necessary and supress NLTK download output
        sys.stdout = open(os.devnull, 'w')
        nltk.data.path.append('./nltk_data')
        # Download the stopwords corpus if not already downloaded
        nltk.download('stopwords', download_dir='./nltk_data', quiet=True)
        sys.stdout = sys.__stdout__
        stop_words = set(stopwords.words("english")) #Get stopwords in English
        tokens = input_clean.split() #Split input in tokens
        filtered_sentence = [word for word in tokens if word.lower() not in stop_words] #Remove stopwords
        query = " AND ".join(filtered_sentence) #Join the remaining tokens with " AND " between them
        query_processed = query
    else: #If there is only one word
        query_processed = input
    return query_processed
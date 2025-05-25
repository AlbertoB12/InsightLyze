"""
# Help-utility to let user select the directory where tweets should be saved
# Program opens a window to facilitate the process
# A folder with the actual date is created to save the tweets
# If no path is selected, program stops
"""

### Packages
import os, sys
from datetime import date
from tkinter import Tk, filedialog
from utils import Show_message
from utils.helpers import config

### Functions
# Main function to save desired directory to save tweets
def save():
    # Initialize tkinter window for better user interface
    root = Tk()
    root.withdraw() #Hide the root window
    # Ask the user to select a directory
    parent_directory = filedialog.askdirectory(title="Select the directory where tweets should be saved. It is "
                                                     "recommended to select the folder 'Saved_tweets in the main script "
                                                     "directory'")
    # If the user selects a directory
    if parent_directory:
        # Create a new folder with the current date
        directory = str(date.today())
        path = os.path.join(parent_directory, directory)
        # Create the directory
        os.makedirs(path, exist_ok=True) #Use os.makedirs to avoid errors if the directory already exists
        Show_message.show_message(f"Directory created: {path}", "Directory Created")
        # Save path to a global variable in config.py
        config.GLOBAL_VARIABLE_SEARCH_TWEETS_PATH = path
        return path
    # If no directory is selected
    else:
        Show_message.show_message("No directory selected. Start the process again", "Selection Error")
        sys.exit(1) #Stop execution
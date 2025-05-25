"""
# Utility to display standard messages in a window
"""

### Packages
from tkinter import Tk, messagebox

### Functions
# Main function to display messages in a tkinter window
# Gets strings (message and title)
def show_message(message, title):
    root = Tk()
    root.withdraw() #Hide the root window
    messagebox.showinfo(title, message) #Display the message
    root.destroy() #Close the root window
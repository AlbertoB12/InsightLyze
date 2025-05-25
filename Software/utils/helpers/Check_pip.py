"""
# Help-utility to check if pip is installed
# If not, user get notification with link to install it
"""

### Packages
import subprocess, sys
import tkinter as tk
from tkinter import messagebox

### Functions
# Function to check if pip is installed
# If not installed, user gets a notification in a window and a guide on how to install it
# If not installed, program stops and user has to run it again after the installation
def check_pip():
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "--version"],
            # Suppress pip version outputs in the console
            stdout=subprocess.DEVNULL, #Suppress stdout
            stderr=subprocess.DEVNULL #Suppress stderr
        )
    except subprocess.CalledProcessError: #If pip cannot be installed
        # Initialize tkinter window
        root = tk.Tk()
        root.withdraw() #Hide the root window
        # Show error message box
        messagebox.showerror(
            "Error: pip Not Installed",
            "pip is not installed. Please install pip and try again.\n\n"
            "You can find the installation guide here: https://pip.pypa.io/en/stable/installation/"
        )
        # Close the tkinter root window
        root.destroy()
        # Exit the program
        sys.exit(1)
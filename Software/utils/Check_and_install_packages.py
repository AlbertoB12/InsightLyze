"""
# Utility to check and install needed packages and versions for the software
"""

### Packages
import subprocess, sys, importlib.metadata
import tkinter as tk
from tkinter import scrolledtext
from utils.helpers import Check_pip

### Functions
# Main function to check the needed packages and install the missing ones
# Checks first if pip is installed
# Opens the txt file containing the required packages
# Checks one by one if the packages are installed
# Installs the missing ones calling the 'install' function
def check_and_install():
    Check_pip.check_pip()
    message = "Checking and installing all necessary packages...\n"
    with open('./utils/helpers/Requirements.txt', 'r', encoding="UTF-8") as requirements: #Open with UTF-8 encoding
        packages = requirements.readlines() #Read every line (every package with the respective version)
    for package in packages:
        package = package.strip()
        # Skip empty lines or malformed lines in the requirements.txt
        if not package or '==' not in package:
            continue
        package_name, version = package.split('==')
        # Check if package with the right version is installed
        try:
            distribution = importlib.metadata.version(package_name)
            if distribution != version:
                message += f"Version mismatch for {package_name}. Installing version {version}...\n"
                install(package_name, version)
        except importlib.metadata.PackageNotFoundError:
            message += f"{package_name} not found. Installing version {version}...\n"
            install(package_name, version)
    message += "Process finished."
    show_message(message, "Process Status")

# Function to display messages in a tkinter window, special for this utility
# Gets string (message)
def show_message(message, title="Information"):
    root = tk.Tk()
    root.title(title)
    # Create a scrolled text widget for displaying messages
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, padx=10, pady=10)
    text_area.pack(padx=20, pady=20)
    text_area.insert(tk.END, message)
    text_area.config(state=tk.DISABLED) #Make the text area read-only
    # Button to close the window
    def close_window():
        root.destroy()
    close_button = tk.Button(root, text="Close", command=close_window)
    close_button.pack(pady=10)
    root.mainloop()

# Function to install a desired package and version using pip
# Gets strings (package and version)
def install(package, version):
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", f"{package}=={version}"],
            # Suppress install outputs in the console
            stdout=subprocess.DEVNULL, #Suppress stdout
            stderr=subprocess.DEVNULL #Suppress stderr
        )
        show_message(f"Successfully installed {package} version {version}.")
    except subprocess.CalledProcessError as e: #Error
        # Show message
        show_message(f"Failed to install {package} version {version}. Error: {e}. Please, try installing it manually.",
                     "Installation Error")
        sys.exit(1)
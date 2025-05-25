"""
# Help-utility to let user introduce his X keys
# Lets user introduce keys if no keys exist
# If keys exist, it lets user decide if he wants to use them, change them or delete them
"""

### Packages
import os, json, sys
from tkinter import Tk, messagebox, simpledialog

# Path where the keys will be saved
keys_file_path = "./utils/helpers/oauth_keys.txt"

### Functions
# Main function to handle key management with a friendly user interface
# Returns dictionary with keys
def manage_keys():
    root = Tk()
    root.withdraw()  #Hide the main window
    # Load keys if existing
    keys = load_keys()
    # If keys exist, ask user if he wants to use them
    if keys:
        use_existing_keys = messagebox.askyesno("Existing Keys Found", "Do you want to use the existing keys?")
        if use_existing_keys:
            root.quit()
            return keys
        # If no, ask if he wants to edit the keys
        edit_keys = messagebox.askyesno("Edit Keys", "Do you want to edit the keys?")
        if edit_keys:
            keys = prompt_for_keys() #Let user introduce new keys
        # If no, stop program
        else:
            print("No keys available to use. Try again later")
            root.quit()
            sys.exit(1)
    # If keys not existing, let user introduce them
    else:
        keys = prompt_for_keys()
    # After all, ask the user if he wants to delete the saved keys
    delete_keys_decision = messagebox.askyesno("Delete Keys", "Do you want to delete the saved keys?")
    if delete_keys_decision:
        delete_keys()
    # Stop window
    root.quit()
    return keys #Return the keys

# Function to load keys from the file
# Returns (if existent) saved keys in file
def load_keys():
    if os.path.exists(keys_file_path):
        with open(keys_file_path, 'r', encoding="UTF-8") as file:
            return json.load(file)

# Function to save keys to the file
# Gets dictionary
def save_keys(keys):
    with open(keys_file_path, 'w', encoding="UTF-8") as file:
        json.dump(keys, file)

# Function to delete the keys file
def delete_keys():
    if os.path.exists(keys_file_path):
        os.remove(keys_file_path)
        messagebox.showinfo("Success", "Keys have been deleted.")
    else:
        messagebox.showinfo("No File", "No keys file found to delete.")

# Function to prompt the user for keys
# Asks user to introduce, one by one, all the keys
# Returns dictionary with keys
def prompt_for_keys():
    keys = {} #To save keys
    # Inputs for the user
    keys['consumer_key'] = simpledialog.askstring("Input", "Enter Consumer Key: ")
    keys['consumer_secret'] = simpledialog.askstring("Input", "Enter Consumer Secret: ")
    keys['access_token'] = simpledialog.askstring("Input", "Enter Access Token: ")
    keys['access_token_secret'] = simpledialog.askstring("Input", "Enter Access Token Secret: ")
    keys['bearer_token'] = simpledialog.askstring("Input", "Enter Bearer Token: ")
    # Ask user if he wants to save keys for future use
    save_keys_decision = messagebox.askyesno("Save Keys", "Do you want to save these keys for future use?")
    if save_keys_decision: #If yes:
        save_keys(keys)
    # If no: nothing is done
    return keys
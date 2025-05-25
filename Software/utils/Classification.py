"""
# Utility to analyse sentiment, emotion and topic of tweets
# It opens a window to get from user: topic of the project and annotation guidelines (for sentiment and emotion analysis)
"""

### Packages
from utils import Show_message, Read_csv
from utils.helpers import Sentiment_analysis, Emotion_analysis, Topic_detection
import pandas as pd
import os
import tkinter as tk
from tkinter import Tk, Label, Entry, Button, messagebox

### Functions
# Main function to classify sentiment, emotion and topic of tweets
# Gets path of tweets (.csv file)
def classification(path):
    Show_message.show_message("Starting the classification process (sentiment, emotion, topic)", "Classification process")
    tweets = Read_csv.read_csv(path) #Read file in directory and get list of strings (tweets to be analysed)
    results = {"Sentiment": [], "Emotion": [], "Topic": []} #Empty dictionary with necessary keys to store results
    # Get information needed for classification
    Show_message.show_message("Please enter more information needed for the classification process", "More info.")
    topic = get_topic() #Topic
    sentiment_guidelines = get_guidelines("Sentiment") #Sentiment guidelines
    emotion_guidelines = get_guidelines("Emotion") #Emotion guidelines
    # Sentiment analysis
    sentiments = Sentiment_analysis.sentiment_analysis(tweets, topic, sentiment_guidelines)
    results["Sentiment"].extend(sentiments) #Add results to the dictionary
    # Emotion analysis
    emotions = Emotion_analysis.emotion_analysis(tweets, topic, emotion_guidelines)
    results["Emotion"].extend(emotions) #Add results to the dictionary
    # Topic detection
    topics = Topic_detection.topic_detection(tweets, topic)
    results["Topic"].extend(topics) #Add results to the dictionary
    # Save classifications
    csv_path = os.path.join(path, "Tweets.csv") #Replace the existing file with the new one
    # Load the .csv file into a DataFrame
    df = pd.read_csv(csv_path, header=None, encoding="UTF-8", sep="|")
    # Add dictionary values to the DataFrame
    df['Sentiment'] = results["Sentiment"]
    df['Emotion'] = results["Emotion"]
    df['Topic'] = results["Topic"]
    # Save the updated DataFrame to a new .csv file
    df.to_csv(csv_path, index=False, encoding="UTF-8", header=False, sep="|") #Separate parts with '|'
    # Display end message
    Show_message.show_message("Classification process terminated", "Classification process")

# Function to get from user the topic of the project
# It opens a window to interact with user
# Retuns string (topic)
def get_topic():
    # Initialize tkinter window for better user interface
    root = Tk()
    root.title("Project topic")
    # Create a label and text entry for user input
    Label(root, text="Enter the topic of your project:").pack(pady=10)
    topic_entry = Entry(root, width=50)
    topic_entry.pack(padx=20, pady=10)
    # Function to be called when the user clicks the "Submit" button
    def on_submit():
        user_input = topic_entry.get()
        if user_input.strip() == "": #If input is empty
            messagebox.showwarning("Input Error", "Please enter a search query.")
        else: #If input is not empty
            # Save input
            root.topic = user_input #Save the input in the root window
            root.quit()
            root.destroy()
    # Submit button
    Button(root, text="Submit", command=on_submit).pack(pady=20)
    root.mainloop()  #Start the tkinter event loop
    return root.topic  #Return the generated input

# Function to get guidelines (for sentiment and emotion analysis) for classification process
# Opens a window to interact with user
# Gets string (type) = "Sentiment" or "Emotion" -> to decide which "submit"-function needs to be used
# Returns dictionary (with answers)
def get_guidelines(type):
    data = {} #Dictionary to store user input
    # Window with submit process
    if type == "Sentiment": #To enter sentiment guidelines
        def submit_sentiment():
            data['positive'] = positive_entry.get() #Introduce positive guidelines
            data['negative'] = negative_entry.get() #Introduce negative guidelines
            data['neutral'] = neutral_entry.get() #Introduce neutral guidelines
            # If something is missing:
            if not data['positive'] or not data['negative'] or not data['neutral']:
                messagebox.showwarning("Input Error", "Please fill in all fields.")
                return
            root.destroy() #Close the window
        # Initialize tkinter window
        root = tk.Tk()
        root.title("Save sentiment analysis guidelines")
        # Create UI components
        tk.Label(root, text="Positive:").pack(pady=5)
        positive_entry = tk.Entry(root, width=50)
        positive_entry.pack(pady=5)
        tk.Label(root, text="Negative:").pack(pady=5)
        negative_entry = tk.Entry(root, width=50)
        negative_entry.pack(pady=5)
        tk.Label(root, text="Neutral:").pack(pady=5)
        neutral_entry = tk.Entry(root, width=50)
        neutral_entry.pack(pady=5)
        tk.Button(root, text="Submit", command=submit_sentiment).pack(pady=20) #Button to save
        root.mainloop() #Finish
    else: #If type == "Emotion"
        def submit_emotion():
            data['happiness'] = happiness_entry.get() #Introduce happiness guidelines
            data['fear'] = fear_entry.get() #Introduce fear guidelines
            data['surprise'] = surprise_entry.get() #Introduce surprise guidelines
            data['sadness'] = sadness_entry.get() #Introduce sadness guidelines
            data['disgust'] = disgust_entry.get() #Introduce disgust guidelines
            data['anger'] = anger_entry.get() #Introduce anger guidelines
            data['frustration'] = frustration_entry.get() #Introduce frustration guidelines
            # If something is missing:
            if not data['happiness'] or not data['fear'] or not data['surprise'] or not data['sadness']\
                    or not data['disgust'] or not data['anger'] or not data['frustration']:
                messagebox.showwarning("Input Error", "Please fill in all fields.")
                return
            root.destroy() #Close the window
        # Initialize tkinter window
        root = tk.Tk()
        root.title("Save emotion analysis guidelines")
        # Create UI components
        tk.Label(root, text="Happiness:").pack(pady=5)
        happiness_entry = tk.Entry(root, width=50)
        happiness_entry.pack(pady=5)
        tk.Label(root, text="Fear:").pack(pady=5)
        fear_entry = tk.Entry(root, width=50)
        fear_entry.pack(pady=5)
        tk.Label(root, text="Surprise:").pack(pady=5)
        surprise_entry = tk.Entry(root, width=50)
        surprise_entry.pack(pady=5)
        tk.Label(root, text="Sadness:").pack(pady=5)
        sadness_entry = tk.Entry(root, width=50)
        sadness_entry.pack(pady=5)
        tk.Label(root, text="Disgust:").pack(pady=5)
        disgust_entry = tk.Entry(root, width=50)
        disgust_entry.pack(pady=5)
        tk.Label(root, text="Anger:").pack(pady=5)
        anger_entry = tk.Entry(root, width=50)
        anger_entry.pack(pady=5)
        tk.Label(root, text="Frustration:").pack(pady=5)
        frustration_entry = tk.Entry(root, width=50)
        frustration_entry.pack(pady=5)
        tk.Button(root, text="Submit", command=submit_emotion).pack(pady=20) #Button to save
        root.mainloop() #Finish
    return data
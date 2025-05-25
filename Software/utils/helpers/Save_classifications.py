"""
# Help-utility to save statistics from classifications (sentiment, emotion and topics)
"""

### Packages
import os
from collections import Counter
import matplotlib.pyplot as plt

### Functions
# Main function to save statistics from classifications (sentiment, emotion and topics)
# Gets path and dataframe
def save_classifications(input, df):
    # Path to save classifications
    # Create new folder to save files
    actual_path = os.path.join(input, "clean")
    path = os.path.join(actual_path, "classifications")
    os.makedirs(path, exist_ok=True) #Use os.makedirs to avoid errors if the directory already exists
    # Sentiments
    # First as text file
    sentiments = df[1].tolist()
    # Lowercase
    sentiments_lower = []
    for sentiment in sentiments:
        sentiments_lower.append(sentiment.lower())
    with open(os.path.join(path, "sentiments.txt"), "w", encoding="UTF-8") as file:
        file.write(str(Counter(sentiments_lower)))
    # Now as graph
    plt.figure(figsize=(10, 6))
    plt.bar(Counter(sentiments_lower).keys(), Counter(sentiments_lower).values())
    plt.xticks(rotation=90)
    plt.xlabel("Sentiment")
    plt.ylabel("Frequency")
    plt.title("Sentiments")
    plt.tight_layout()
    plt.savefig(os.path.join(path, "sentiments_plot.png"), format='png')
    plt.close()
    # Emotions
    # First as text file
    emotions = df[2].tolist()
    # Lowercase
    emotions_lower = []
    for emotion in emotions:
        emotions_lower.append(emotion.lower())
    with open(os.path.join(path, "emotions.txt"), "w", encoding="UTF-8") as file:
        file.write(str(Counter(emotions_lower)))
    # Now as graph
    plt.figure(figsize=(10, 6))
    plt.bar(Counter(emotions_lower).keys(), Counter(emotions_lower).values())
    plt.xticks(rotation=90)
    plt.xlabel("Emotion")
    plt.ylabel("Frequency")
    plt.title("Emotions")
    plt.tight_layout()
    plt.savefig(os.path.join(path, "emotions_plot.png"), format='png')
    plt.close()
    # Topics
    # First as text file
    topics = df[3].tolist()
    # Split each line by commas, convert to lowercase, and strip white spaces
    topics_lower = [topic.lower().strip() for line in topics for topic in line.split(',')]
    with open(os.path.join(path, "topics.txt"), "w", encoding="UTF-8") as file:
        file.write(str(Counter(topics_lower)))
    # Get the top 15 most common topics to be displayed
    top_15_topics = Counter(topics_lower).most_common(15)
    # Now as graph
    plt.figure(figsize=(10, 6))
    topics, frequencies = zip(*top_15_topics) #Unzip the topics and frequencies
    plt.bar(topics, frequencies)
    plt.xticks(rotation=90)
    plt.xlabel("Topic")
    plt.ylabel("Frequency")
    plt.title("Top 15 Topics")
    plt.tight_layout()
    plt.savefig(os.path.join(path, "topics_plot.png"), format='png')
    plt.close()
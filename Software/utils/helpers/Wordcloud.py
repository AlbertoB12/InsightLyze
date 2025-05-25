"""
# Help-utility to create wordcloud from unigrams
"""

### Packages
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

### Functions
# Main function to create wordcloud from unigrams
# Gets path and dictionary
def wordcloud(path, unigrams):
    # Path to save wordcloud
    # Create new folder to save files
    actual_path = os.path.join(path, "clean")
    path = os.path.join(actual_path, "wordcloud")
    os.makedirs(path, exist_ok=True) #Use os.makedirs to avoid errors if the directory already exists
    # Unigram wordcloud
    unigrams_wordcloud = WordCloud(background_color="white", max_words=50).generate_from_frequencies(unigrams)
    plt.figure(figsize=(12, 8))
    plt.imshow(unigrams_wordcloud, interpolation="bilinear")
    plt.title("Unigrams")
    plt.axis("off")
    plt.savefig(os.path.join(path, "unigrams_wordlocud.png"), format='png') #Save the plot as a PNG file
    plt.close()
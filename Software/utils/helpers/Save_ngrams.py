"""
# Help-utility to save n_grams (uni, bi and trigrams) as text files and graphs
"""

### Packages
import os
import matplotlib.pyplot as plt

### Functions
# Main function to save n_grams (uni, bi and trigrams) as text files and graphs
# Gets path and unigrams, bigrams and trigrams as dictionaries
def save_ngrams(path, unigrams, bigrams, trigrams):
    # Create new folder to save files
    actual_path = os.path.join(path, "clean")
    path = os.path.join(actual_path, "n_grams")
    os.makedirs(path, exist_ok=True) #Use os.makedirs to avoid errors if the directory already exists
    # Save text files
    save_ngrams_text(path, unigrams, bigrams, trigrams)
    # Save graphs
    save_ngrams_graphs(path, unigrams, bigrams, trigrams)

# Function to save n_grams as graphs
# Gets path, unigrams, bigrams, trigrams
def save_ngrams_graphs(path, unigrams, bigrams, trigrams):
    # Unigrams
    plt.bar(*zip(*unigrams.most_common(15)))
    plt.xticks(rotation=90)
    plt.xlabel("Unigram")
    plt.ylabel("Frequency")
    plt.title("Unigrams")
    plt.tight_layout()
    plt.savefig(os.path.join(path, "unigrams_plot.png"), format='png') #Save the plot as a PNG file
    # Bigrams
    wrds_bi_a = ['-'.join(x) for x, c in bigrams.most_common(15)] #Join the 2 words with '-' in the middle
    wdth_bi_a = [c for x, c in bigrams.most_common(15)] #Get the counts
    plt.bar(wrds_bi_a, wdth_bi_a, color='blue')
    plt.xticks(rotation=90)
    plt.title("Bigrams")
    plt.xlabel("Bigram")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(os.path.join(path, "bigrams_plot.png"), format='png') #Save the plot as a PNG file
    # Trigrams
    wrds_tri_a = ['-'.join(x) for x, c in trigrams.most_common(15)]
    # get the counts
    wdth_tri_a = [c for x, c in trigrams.most_common(15)]
    plt.bar(wrds_tri_a, wdth_tri_a, color='blue')
    plt.xticks(rotation=90)
    plt.title("Trigrams")
    plt.xlabel("Trigram")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(os.path.join(path, "trigrams_plot.png"), format='png') #Save the plot as a PNG file

# Function to save n_grams as text files
# Gets path, unigrams, bigrams, trigrams
def save_ngrams_text(path, unigrams, bigrams, trigrams):
    for i in range(3):  # 3 new files
        if i == 0:
            with open(os.path.join(path, "unigrams.txt"), "w", encoding="UTF-8") as file:
                file.write(str(unigrams))
        if i == 1:
            with open(os.path.join(path, "bigrams.txt"), "w", encoding="UTF-8") as file:
                file.write(str(bigrams))
        if i == 2:
            with open(os.path.join(path, "trigrams.txt"), "w", encoding="UTF-8") as file:
                file.write(str(trigrams))
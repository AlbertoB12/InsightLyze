"""
# Help-utility to get sentiments of tweets
# Uses LLM and prompt engineering
"""

### Packages
from transformers import pipeline
import os
from utils import Show_message

### Functions
# Main function to get the sentiment of a tweet
# Uses LLM and prompt engineering
# Gets a list of strings
# Returns a list of strings (sentiments)
def sentiment_analysis(tweets, topic, guidelines):
    Show_message.show_message("Analysing sentiment", "Sentiment")
    sentiments = [] #Empty list to be returned
    for tweet in tweets: #Analyse one by one
        messages = [
            {"role": "user",
            "content": f"""Below is an input ('Instruction') of a user of a chatbot specialized in sentiment analysis 
            consisting of a tweet with the topic '{topic}'. Write a response with the sentiment of this tweet, but only 
            one word with the sentiment ('Positive', 'Negative', 'Neutral'). If the tweet has no direct reference to the
             topic ('{topic}'), write (only the word)'NO' as response.
             
            Here you have annotation guidelines:
            Positive: {guidelines['positive']}.
            Negative: {guidelines['negative']}.
            Neutral: {guidelines['neutral']}.
            
            The tweet is: '{tweet}'."""}, #Prompt
        ]
        # Create absolute model path
        model_path = r".\llms\models--meta-llama--Meta-Llama-3.1-8B-Instruct\snapshots\5206a32e0bd3067aef1ce90f5528ade7d866253f"
        model_path = os.path.abspath(model_path)
        # Answer generation
        pipe = pipeline("text-generation",
                        model=model_path,
                        trust_remote_code=True)
        response = pipe(messages, max_new_tokens=1)
        sentiment = response[0]['generated_text'] #Answer
        first_word = sentiment.split()[0] if sentiment else '' #If LLM returns more than one word, keep only the first one
        sentiments.append(first_word)
        Show_message.show_message("Sentiment analysed", "Done")
    return sentiments

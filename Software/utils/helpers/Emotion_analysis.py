"""
# Help-utility to get emotions of tweets
# Emotions: Joy, trust, fear, surprise, sadness, disgust, anger, anticipation, frustration
# Uses LLM and prompt engineering
"""

### Packages
from transformers import pipeline
import os
from utils import Show_message

### Functions
# Main function to get the emotion of a tweet
# Uses LLM and prompt engineering
# Gets a list of strings
# Returns a list of strings (emotions)
def emotion_analysis(tweets, topic, guidelines):
    Show_message.show_message("Analysing emotion", "Emotion")
    emotions = [] #Empty list to be returned
    for tweet in tweets: #Analyse one by one
        messages = [
            {"role": "user",
             "content": f"""Below is an input ('Instruction') of a user of a chatbot specialized in Emotion analysis 
             consisting of a tweet with the topic '{topic}'. Write a response with the emotion of this tweet, but only 
             one word with the emotion ('joy', 'trust', 'fear', 'surprise', 'sadness', 'disgust', 'anger', 'anticipation', 'frustration'), 
             that means that the response will only have ONE WORD with the emotion, give no more explanations.
            Here you have annotation guidelines:
            Happiness: {guidelines['happiness']}.
            Fear: {guidelines['fear']}.
            Surprise: {guidelines['surprise']}.
            Sadness: {guidelines['sadness']}.
            Disgust: {guidelines['disgust']}.
            Anger: {guidelines['anger']}.
	    Frustration: {guidelines['frustration']}.

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
        emotion = response[0]['generated_text'] #Answer
        first_word = emotion.split()[0] if emotion else '' #If LLM returns more than one word, keep only the first one
        emotions.append(first_word)
        Show_message.show_message("Emotion analysed", "Done")
    return emotions
"""
# Help-utility to get topic of tweets
# Uses LLM and prompt engineering
"""

### Packages
from transformers import pipeline
import os
from utils import Show_message

### Functions
# Main function to get the topic of a tweet
# Uses LLM and prompt engineering
# Gets a list of strings
# Returns a list of strings (topics)
def topic_detection(tweets, topic):
    Show_message.show_message("Analysing topics", "Topic")
    topics = [] #Empty list to be returned
    for tweet in tweets: #Analyse one by one
        messages = [
            {"role": "user",
             "content": f"""Below is an input ('Instruction') of a user of a chatbot specialized in topic detection 
             consisting of a tweet with the topic '{topic}'. Write a response with the topic(s) of this tweet only with
              one or more topics, no explanations. The tweet is: {tweet}"""}, #Prompt
        ]
        # Create absolute model path
        model_path = r".\llms\models--meta-llama--Meta-Llama-3.1-8B-Instruct\snapshots\5206a32e0bd3067aef1ce90f5528ade7d866253f"
        model_path = os.path.abspath(model_path)
        # Answer generation
        pipe = pipeline("text-generation",
                        model=model_path,
                        trust_remote_code=True)
        response = pipe(messages, max_new_tokens=1)
        topic = response[0]['generated_text'] #Answer
        topics.append(topic)
        Show_message.show_message("Topics analysed", "Done")
    return topics
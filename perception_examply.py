from transformers import pipeline

# Setup a sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")


# Agent perceives user input
user_input = "I'm having a wonderful day!"
result = sentiment_analyzer(user_input)
print("User sentiment: ",result[0])
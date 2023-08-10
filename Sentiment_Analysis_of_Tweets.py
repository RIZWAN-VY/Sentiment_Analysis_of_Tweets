"""
THIS IS A SENTIMENT ANALYSIS PROGRAM THAT PARSES THE TWEETS FETCHED FROM TWITTER USING PYTHON
"""
# Import necessary libraries
import tweepy
from textblob import TextBlob
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from time import sleep

# Import Twitter API credentials
from API_keys_Tokens import API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Authenticate and create the Tweepy API object
authenticate = tweepy.OAuthHandler(API_KEY,API_KEY_SECRET)
authenticate.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
API = tweepy.API(authenticate)

# Function to clean tweets from unwanted elements
def tweets_cleaning(text):
    text = re.sub(r"http\S+|www\S+|https\S+|RT", '', text, flags=re.MULTILINE)  # Remove URLs
    text = re.sub(r'[^\w\s]', '', text)     # Remove special characters and numbers
    text = text.lower()     # Convert to lowercase for accurate sentiment analysis
    return text

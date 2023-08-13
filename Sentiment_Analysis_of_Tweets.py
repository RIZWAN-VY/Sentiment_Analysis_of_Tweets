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
try:
    # Code that may cause an error
    authenticate = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    authenticate.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(authenticate)

except tweepy.error.TweepError:
    print("Error connecting to Twitter API")

else:
    print("Successfully connected to Twitter API")

# Function to clean tweets from unwanted elements
def tweets_cleaning(text):
    text = re.sub(r"http\S+|www\S+|https\S+|RT", '', text, flags=re.MULTILINE)  # Remove URLs
    text = re.sub(r'[^\w\s]', '', text)     # Remove special characters and numbers
    text = text.lower()     # Convert to lowercase for accurate sentiment analysis
    return text

# 1) Function to Calculates and prints the total count of each sentiment of tweets
def sentiment_count(tweets):
    print("\nprinting sentiment count of tweets based on your keyword..........")
    sleep(3)
    positive_count = 0
    negative_count = 0
    neutral_count = 0
    for twt in tweets:
        tweet =  twt.text 
        cleaned_tweet = tweets_cleaning(tweet)
        analysis = TextBlob(cleaned_tweet)
        if analysis.sentiment.polarity > 0:
            positive_count += 1
        elif analysis.sentiment.polarity < 0:
            negative_count += 1
        else:
            neutral_count += 1
    total_count = positive_count + negative_count + neutral_count
    print("Total Positive Tweets:", positive_count)
    print("Total Negative Tweets:", negative_count)
    print("Total Neutral Tweets:", neutral_count)
    print("Total Tweets:",total_count)

# 2) Function to print all tweets with sentiment and total count
def All_Tweets(tweets):
    print("\nprinting all tweets with sentiment and total count based on your keyword..........")
    sleep(3)
    total_count = 0
    i = 1

    for twt in tweets:
        tweet =  twt.text 

        # Preprocess the tweet text
        cleaned_tweet = tweets_cleaning(tweet)
        print(str(i) + ") " + cleaned_tweet + "\n")

        # Sentiment Analysis of Tweets
        analysis = TextBlob(cleaned_tweet)
        if analysis.sentiment.polarity > 0:
            print("This is a positive tweet")
            print("----------------------------------------")

        elif analysis.sentiment.polarity < 0:
            print("This is a negative tweet")
            print("----------------------------------------")

        else:
            print("This is a neutral tweet")
            print("----------------------------------------")
        total_count += 1
        i += 1
    print("Total Tweets:",total_count)

# Function to analyze sentiment of tweets
def analyze_sentiment(tweet_text):
    cleaned_tweet = tweets_cleaning(tweet_text)
    analysis = TextBlob(cleaned_tweet)
    
    if analysis.sentiment.polarity > 0:
        return "positive"
    elif analysis.sentiment.polarity < 0:
        return "negative"
    else:
        return "neutral"
    
#  Function to analyze tweets based on desired sentiment
def analyze_tweets_by_sentiment(Tweets, desired_sentiment):
    print(f"\nPrinting {desired_sentiment} tweets and its count based on your keyword..........")
    sleep(3)
    count = 0
    i = 1
    
    for twt in Tweets:
        tweet = twt.text
        cleaned_tweet = tweets_cleaning(tweet)
        sentiment = analyze_sentiment(cleaned_tweet)
        
        if sentiment == desired_sentiment:
            print(str(i) + ") " + cleaned_tweet + "\n")
            print(f"This is a {desired_sentiment} tweet")
            count += 1
            print("----------------------------------------")
        i += 1
    print(f"Total {desired_sentiment.capitalize()} Tweets:", count)

#  3) Positive_Tweets   
def Positive_Tweets(Tweets):
    analyze_tweets_by_sentiment(Tweets, "positive")

#  4) Negative_Tweets
def Negative_Tweets(Tweets):
    analyze_tweets_by_sentiment(Tweets, "negative")

#  5)  Neutral_Tweets
def Neutral_Tweets(Tweets):
    analyze_tweets_by_sentiment(Tweets, "neutral")

# 6) Function to generates a bar chart to visualize sentiment distribution
def sentiment_chart(Tweets):
    print("\nGenerating Sentiment chart......................")
    sleep(3)
    positive_count = 0
    negative_count = 0
    neutral_count = 0    
    for twt in Tweets:
        tweet =  twt.text 
        cleaned_tweet = tweets_cleaning(tweet)
        analysis = TextBlob(cleaned_tweet)
        if analysis.sentiment.polarity > 0:
            positive_count += 1
        elif analysis.sentiment.polarity < 0:
            negative_count += 1
        else:
            neutral_count += 1
            
    # Visualization (Create a bar chart) of Positive,Negative and Neutral Tweets
    sentiment_labels = ['Positive','Neutral','Negative']
    sentiment_counts = [positive_count,neutral_count,negative_count]
    plt.bar(sentiment_labels, sentiment_counts, color=['green', 'blue' , 'red'])
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.title('Sentiment Analysis of Tweets')
    plt.show()
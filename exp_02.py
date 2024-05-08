import tweepy

# Set up your Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Scrape tweets from a user's timeline
username = "twitter_username"
tweets = api.user_timeline(screen_name=username, count=10)

# Print the scraped tweets
for tweet in tweets:
    print(tweet.text)
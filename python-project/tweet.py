import twitter
import random

# connect to twitter
api = twitter.Api(consumer_key="consumer key", 
                  consumer_secret="consumer secret", 
                  access_token_key="access token key", 
                  access_token_secret="access token secret", 
                  access_token_secret="access token secret")

# Get tweeter followers
def get_followers():
     # Get followers
     # Return followers
    followers = api.GetFollowers()
    return followers

followers = get_followers()

# Pick one at random
random_index = random.randint(0, len(followers) - 1)
random_follower = followers[random_index]

# Tweet at the random follower
tweet = "@{} you are the random follower of the day!".format(random_follower.screen_name)   
print(tweet)
api.PostUpdate(tweet)
print("Tweeted!")

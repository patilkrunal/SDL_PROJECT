import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

#Authentication with twitter API
consumer_key = 'wJfTjhAhS1F2eac84zBl0VgZ0'
consumer_secret = 'IuQLvzWrk1fgetrRO9xTKLwZp1JaL4KpmYcaPtbmPJkEMTIfXc'

access_token = '1459989746-mGMuvbiltJalHzwzaGPXhf37lTlXnlb1H217ij1'
access_token_secret = 'LCRnyj4Cuwr5BSgJA6zlCuKAc5IA8TMHl4HKdheUdMp06'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Keyword of which sentiment to be calculated is taken from user
value = input("Enter the keyword:")

#tweets containing keyword are collected
public_tweets = api.search(value) 

#list initialized to calculate total sentiments(polarity)
total_pol = []
k = 0

#tweets are printed along with its individual sentiments score
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    total_pol.insert(k, analysis.sentiment.polarity)
    k += 1
j = 0
n = 0
for i in total_pol:
    j = j + i
    n = n + 1

p = j/n


print("Total sentiments score(-1 to 1): ",p)

v = ((1+p)*100)/2

#Plotting obtained score in pie chart
labels = 'likes', 'dislikes'
sizes = [v,100-v ]
color = ['lightskyblue', 'yellowgreen']
explode = (0.1, 0)

plt.pie(sizes, explode = explode, labels = labels, colors = color, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()

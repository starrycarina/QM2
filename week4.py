sample = tweets.head(3000)
sample['polarity'] = sample['text'].apply(lambda x: nlp(x)._.blob.polarity)
sample['subjectivity'] = sample['text'].apply(lambda x: nlp(x)._.blob.subjectivity)
filtered_sample = sample[(sample['subjectivity'] > 0.5) & (sample['polarity'] < 0)]
print(filtered_sample)

user_sentiment = filtered_sample.groupby('author_id')['polarity'].sum()
min_polarity = user_sentiment.min()
user_with_min_polarity = user_sentiment.idxmin()

print("User ID with the lowest total sentiment:", user_with_min_polarity)
print("Lowest total sentiment:", min_polarity)

# Get all tweets of the user with minimum polarity
user_tweets = tweets[tweets['author_id'] == user_with_min_polarity]['text']

# Print the tweets
for tweet in user_tweets:
    print(tweet)

from scipy.stats import ttest_ind

# Load the data
tweets = pd.read_csv('https://storage.googleapis.com/qm2/wk7/elon_twitter.csv')
tweets['hour'] = pd.to_datetime(tweets['hour'])

# Define the event date
tweet = datetime.datetime(2022, 10, 28)

# Separate the data into before and after groups
before = tweets[tweets['hour'] < tweet]['count']
after = tweets[tweets['hour'] > tweet]['count']

# 1. State the hypotheses:
# H0: There is no significant difference in the average number of slur-containing tweets before and after Elon Musk's tweet.
# Ha: There is a significant increase in the average number of slur-containing tweets after Elon Musk's tweet.

# 2. Set the significance level (alpha):
alpha = 0.05

# 3. Calculate the test statistic and p-value:
t_statistic, p_value = ttest_ind(before, after)

print("T-statistic:", t_statistic)
print("P-value:", p_value)

# 4. Make a decision:
if p_value < alpha:
    print("Reject the null hypothesis.")
    print("There is evidence to suggest a significant increase in hate speech after Elon Musk's tweet.")
else:
    print("Fail to reject the null hypothesis.")
    print("There is not enough evidence to suggest a significant increase in hate speech after Elon Musk's tweet.")

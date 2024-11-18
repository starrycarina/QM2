# prompt: This plot definitely shows an uptick in the number of tweets containing a racial slur following Musk's tweet. But is this increase statistically significant?
# Question: Using a t-test and the full hypothesis testing procedure, investigate wheter there was a statistically significant increase in hate speech following Elon Musk's tweet. Make note of the T statistic and the P value
import pandas as pd
import datetime
from matplotlib.pyplot import figure
import matplotlib.dates as mdates
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

# Previous code to define 'tweets' should be run before this cell
# The following line assumes it was defined in a previous cell and reads from the same CSV file
tweets = pd.read_csv('https://storage.googleapis.com/qm2/wk7/elon_twitter.csv') # read in the data
tweets['hour'] = pd.to_datetime(tweets['hour'])
tweet = datetime.datetime(2022, 10, 28)


# Separate the data into pre and post Elon Musk's tweet
pre_elon = tweets[tweets['hour'] < tweet]['count']
post_elon = tweets[tweets['hour'] > tweet]['count']

# Perform an independent samples t-test
t_statistic, p_value = ttest_ind(pre_elon, post_elon)

# Print the results
print("T-statistic:", t_statistic)
print("P-value:", p_value)

# Interpret the results
alpha = 0.05  # Significance level
if p_value < alpha:
    print("The difference in the mean number of tweets containing a racial slur is statistically significant.")
else:
    print("The difference in the mean number of tweets containing a racial slur is not statistically significant.")

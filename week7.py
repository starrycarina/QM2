# Filter for construction, extraction, and installation occupations
filtered_df = reg_df[reg_df['occupation'] == 'Consruction, Extraction, Installation']

import numpy as np

# Filter for union == 2.0
union_2 = filtered_df[filtered_df['union'] == 2.0]

# Filter for union == 3.0
union_3 = filtered_df[filtered_df['union'] == 3.0]

# Calculate the log of realhrwage for both groups
log_realhrwage_2 = np.log(union_2['realhrwage'])
log_realhrwage_3 = np.log(union_3['realhrwage'])


# Calculate the difference in means of log realhrwage between the two groups
difference_in_means = np.mean(log_realhrwage_2) - np.mean(log_realhrwage_3)

print(f"The difference in means of log realhrwage between union == 2.0 and union == 3.0 is: {difference_in_means}")

from scipy.stats import ttest_ind

# Perform an independent samples t-test
t_statistic, p_value = ttest_ind(log_realhrwage_2, log_realhrwage_3)

print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")

alpha = 0.05  # Significance level

if p_value < alpha:
    print("The difference in means is statistically significant.")
else:
    print("The difference in means is not statistically significant.")

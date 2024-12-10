# Create the necessary variables
did2['post'] = np.where(did2['date'] >= '2007-01-01', 1, 0)
did2['treatment'] = np.where(did2['state'] == 'arizona', 1, 0)
did2['post_treatment'] = did2['post'] * did2['treatment']

# Run the difference-in-differences regression
did_model2 = ols('unemployment ~ post + treatment + post_treatment', data=did2).fit()
print(did_model2.summary())

# The coefficient for 'post_treatment' in the did_model2 summary represents the effect of the minimum wage increase on unemployment in Arizona compared to Louisiana.

# Extract the coefficient and its p-value
treatment_effect = did_model2.params['post_treatment']
p_value = did_model2.pvalues['post_treatment']

print(f"The effect of the minimum wage increase on unemployment in Arizona (compared to Louisiana) is {treatment_effect:.3f}.")
print(f"The p-value for this effect is {p_value:.3f}.")

# Interpretation:
# If the p-value is less than 0.05 (a common significance level), we can reject the null hypothesis that there's no effect.  
# A positive treatment effect suggests that Arizona's unemployment increased relative to Louisiana after the minimum wage hike. A negative effect suggests a decrease.


# The 2008 financial crisis is a major event that likely violates the "no simultaneous treatment" assumption.  The crisis triggered a global recession, significantly impacting employment rates across various countries and states, including Arizona and Louisiana.  This external shock constitutes a simultaneous treatment, confounding the impact of Arizona's minimum wage increase on its unemployment rate. It's difficult to isolate the effect of the minimum wage change from the broader economic downturn.

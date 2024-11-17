import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy.stats import t 

def modified_two_hist(groups, group_labs, xlab, title):
    plt.figure(figsize=(15, 6))

    sample_means_list = []  # List to store sample means for each group

    for i, var in enumerate(groups):
        sample_size = 1000
        sample_means = []
        iterations = 10000

        for _ in range(iterations):
            sample = var.sample(sample_size, replace=True)
            sample_mean = sample.mean()
            sample_means.append(sample_mean)

        sample_means_list.append(sample_means)  # Append sample means for this group
        
        # Move the confidence interval calculation outside the loop
        if len(sample_means_list) == len(groups):  # Calculate only after processing all groups
            lower_ci, upper_ci = calculate_confidence_interval(sample_means_list)
            print(f"95% Confidence Interval for Difference in Means: ({lower_ci:.2f}, {upper_ci:.2f})")


        plt.hist(sample_means, bins=int(iterations / 300), edgecolor='white', density=True, label=group_labs[i])
        mu, se = norm.fit(sample_means)
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mu, se)

        mean = var.mean()
        lower_ci = mu - se * 1.96
        upper_ci = mu + se * 1.96

        plt.plot(x, p, 'k', linewidth=2)
        plt.xlabel(xlab)
        plt.title(title)
        plt.axvline(mean, color='green', linestyle='solid', linewidth=3)
        plt.axvline(lower_ci, color='black', linestyle='dashed', linewidth=1.5)
        plt.axvline(upper_ci, color='black', linestyle='dashed', linewidth=1.5)
        plt.legend()

    # Calculate absolute difference in population means
    pop_mean_diff = abs(np.mean(sample_means_list[0]) - np.mean(sample_means_list[1]))
    print(f"Absolute Difference in Population Means: {int(round(pop_mean_diff))}")

    plt.show()


def calculate_confidence_interval(sample_means_list):
    mean1 = np.mean(sample_means_list[0])
    mean2 = np.mean(sample_means_list[1])
    diff_means = mean1 - mean2
    se_diff = np.sqrt(np.var(sample_means_list[0]) / len(sample_means_list[0]) + 
                      np.var(sample_means_list[1]) / len(sample_means_list[1]))

    # Calculate 95% confidence interval using t-distribution
    df = len(sample_means_list[0]) + len(sample_means_list[1]) - 2  # Degrees of freedom
    t_critical = t.ppf(0.975, df)  # Critical value for 95% confidence
    margin_of_error = t_critical * se_diff
    lower_ci = diff_means - margin_of_error
    upper_ci = diff_means + margin_of_error

    return lower_ci, upper_ci


modified_two_hist([whitemenHS,hispanicwomenBA], ['White Men with a High School Diploma','Hispanic Women with a Bachelors'],'Income ($, thousands)', "Income Sample Means")


whitemenHS=df[(df['sex']==1) & (df['race']==1) & (df['sch']==12)]['income']
hispanicwomenBA = df[(df['sex']==2) & (df['race']==3) & (df['sch']==14)]['income']

modified_two_hist([whitemenHS,hispanicwomenBA], ['White Men with a High School Diploma','Hispanic Women with a Bachelors'],'Income ($, thousands)', "Income Sample Means")

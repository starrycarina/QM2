import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

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

whitemenHS=df[(df['sex']==1) & (df['race']==1) & (df['sch']==12)]['income']
hispanicwomenBA = df[(df['sex']==2) & (df['race']==3) & (df['sch']==14)]['income']

modified_two_hist([whitemenHS,hispanicwomenBA], ['White Men with a High School Diploma','Hispanic Women with a Bachelors'],'Income ($, thousands)', "Income Sample Means")

# prompt: Try fitting the following models:
# Linear, Same Slopes

import warnings
import pandas as pd
import numpy as np
from matplotlib import style
from matplotlib import pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import geopandas as gpd
from statsmodels.formula.api import ols
from ipyleaflet import Map, Marker, basemaps, basemap_to_tiles

# ... (rest of the provided code)

# 1. Linear, Same Slopes
rdd_df = drinking.assign(threshold=(drinking["agecell"] > 0).astype(int))
model_same_slopes = smf.wls("all ~ agecell + threshold", rdd_df).fit() 
print(model_same_slopes.summary())

ate_pct_same_slopes = 100 * (model_same_slopes.params["threshold"] / model_same_slopes.params["Intercept"] )

print("Alcohol increases the chance of death by all causes by {}% (Same Slopes)".format(np.round(ate_pct_same_slopes, 2)))

ax = drinking.plot.scatter(x="agecell", y="all", color="C0")
drinking.assign(predictions=model_same_slopes.fittedvalues).plot(x="agecell", y="predictions", ax=ax, color="C1")
plt.title(f"Impact of Alcohol on Death (Same Slopes): {np.round(ate_pct_same_slopes, 2)}% \n p={np.round(model_same_slopes.pvalues['threshold'], 3)}, R2={np.round(model_same_slopes.rsquared, 3)}")
plt.show()


# ... (previous imports and code)

# 2. Linear, Different Slopes
model_different_slopes = smf.wls("all~ agecell * threshold ", rdd_df).fit()  
print(model_different_slopes.summary())

# Visualization for Different Slopes Model:
ax = drinking.plot.scatter(x="agecell", y="all", color="C0") # Scatter plot of original data
drinking.assign(predictions=model_different_slopes.fittedvalues).plot(
    x="agecell", y="predictions", ax=ax, color="C1" 
)  # Overlay predicted values
plt.title("Impact of Alcohol on Death (Different Slopes)")
plt.xlabel("Age Centered at 21") 
plt.ylabel("Mortality Rate (All Causes)")
plt.show()

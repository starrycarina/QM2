
# Filter for construction, extraction, and installation occupations (occupation code 7)
filtered_df = reg_df[reg_df['occupation'] == 'Consruction, Extraction, Installation']

# Check if the filtered dataframe has any observations with union information and sufficient union categories
if filtered_df.shape[0] > 0 and filtered_df['union'].notna().any() and len(filtered_df['union'].unique()) > 1:
    # Ensure 'union' is treated as categorical
    filtered_df['union'] = pd.Categorical(filtered_df['union'])  
    
    # Create the regression model with logwage as the dependent variable and union as the independent variable
    model = ols('logwage ~ C(union)', data=filtered_df).fit()

    # Get the coefficient and p-value for union members (union code 2) compared to those covered by union (union code 3)
    try:
        # Extract the coefficient for union members (union code 2) compared to the reference category 
        union_member_coef = model.params['C(union)[T.2]']  
        union_member_p_value = model.pvalues['C(union)[T.2]']

        # Assuming union code 3 (covered by union) is the base category
        # Note that union code 1 is the default base category for statsmodels
        # if not explicitly defined to be otherwise.
        reference_category = 3 
        
    except KeyError:  # If union code 2 is missing, print an informative message
        print("Error: Cannot find coefficient for union members (union code 2).")
        union_member_coef = np.nan # Set a default value
        union_member_p_value = np.nan # Set a default value
        reference_category = "N/A" # Set a default value
        
    print(f"Difference in log hourly earnings for union members (code 2) compared to those covered by union (code {reference_category}): {union_member_coef:.3f}")
    print(f"P-value: {union_member_p_value:.3f}")

    if union_member_p_value < 0.05:
        print("The difference is statistically significant at the 5% level.")
    else:
        print("The difference is not statistically significant at the 5% level.")
else:
    print("No data available for the specified occupation and union membership or insufficient union categories for comparison.")

# regenerate daily dataframe using 'Date' column
daily = df.groupby('Date')['AQI'].mean().reset_index()

# sort by AQI in descending order
daily_sorted = daily.sort_values('AQI', ascending=False)

# get the date with the second-worst AQI
second_worst_date = daily_sorted.iloc[1]['Date']

from datetime import datetime
second_worst_date = datetime.strptime(second_worst_date, '%m/%d/%y').strftime('%d-%m-%Y')  

# display
print(f"The date with the second-worst AQI is: {second_worst_date}")  
satellite_plot(second_worst_date)

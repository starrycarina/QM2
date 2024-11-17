# scrape the table of Nobel Laureates in Chemistry using read_html. remember, this gives us a LIST of dataframes! lets call this list chem_tables

import pandas as pd
chem_tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_Nobel_laureates_in_Chemistry")  

# select the first dataframe from this list and call it chem

chem = chem_tables[0]
print(chem)

# create a new dataframe called 'country' in which each row is a country, and the values represent the number of nobel laureates. 

country = chem.groupby('Nationality[B]').size().reset_index(name='counts')

## cleaning based on the text data we have

cleaned_country = country
cleaned_country = cleaned_country[cleaned_country['Nationality[B]'] != 'Not awarded'] # remove 'not awarded' from the data
cleaned_country = cleaned_country.replace('  ', ';', regex=True) # shows dual nationalities as nationality a;nationality b
cleaned_country = cleaned_country.replace('West German', 'German', regex=True)
cleaned_country = cleaned_country.replace('\[', '', regex=True)
cleaned_country = cleaned_country.replace('\]', '', regex=True)
cleaned_country = cleaned_country.replace('0', '', regex=True)
cleaned_country = cleaned_country.replace('1', '', regex=True)
cleaned_country = cleaned_country.replace('2', '', regex=True)
cleaned_country = cleaned_country.replace('5', '', regex=True)
cleaned_country = cleaned_country.replace('7', '', regex=True)
cleaned_country = cleaned_country.replace('8', '', regex=True)

## split dual nationalities and create a new dataframe
all_nationalities = []
for index, row in cleaned_country.iterrows():
    nationalities = row['Nationality[B]'].split(';')  # split by semicolon
    for nationality in nationalities:
        all_nationalities.append({'Country': nationality, 'counts': row['counts']})

split_country = pd.DataFrame(all_nationalities)

## group by country and sum counts

final_country = split_country.groupby('Country')['counts'].sum().reset_index()

# now sort it in descending order

final_country = final_country.sort_values(by=['counts'], ascending=False)
print(final_country)

# finally, plot the top 10 countries

import matplotlib.pyplot as plt
top_10_countries = final_country.head(10)
plt.bar(top_10_countries['Country'], top_10_countries['counts'])

plt.title('Top 10 Countries by Number of Nobel Laureates in Chemistry')
plt.xlabel('Country')
plt.ylabel('Number of Laureates')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent labels from overlapping

plt.show()

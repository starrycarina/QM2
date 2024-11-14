import pandas

!mkdir -p ./data/wk1
!curl https://storage.googleapis.com/qm2/wk1/spotify-2023.csv -o ./data/wk1/spotify-2023.csv


data = pandas.read_csv('./data/wk1/spotify-2023.csv') # Updated path to the correct location
data = data.rename(columns={'streams': 'bpm', 'bpm': 'streams'})

desired_key = 'C#'
filtered_data = data[data['key'] == desired_key]

filtered_data.sort_values(by='streams', ascending=False).head()

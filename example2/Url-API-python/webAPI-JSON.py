import sys
import requests
import eia

# Json format
link = "http://api.eia.gov/series/?series_id=NG.N9010US2.M&api_key=xxxx&out=json"
f = requests.get(link)

print(f.text)


import sys
import requests
import eia
import pandas as pd

# API Key from EIA
api_key = 'xxxxx'

# PADD Names to Label Columns
# Change to whatever column labels you want to use.
PADD_NAMES = ['PADD 1','PADD 2','PADD 3','PADD 4','PADD 5']

# Series IDs 
PADD_KEY = [
    'PET.MCRRIP12.M',
    'PET.MCRRIP22.M',
    'PET.MCRRIP32.M',
    'PET.MCRRIP42.M',
    'PET.MCRRIP52.M']

# Initialize list - this is the final list that we will store all the data from the json pull. Then we will use this list to concat into a pandas dataframe. 
final_data = []

# start and end dates
startDate = '2009-01-01'
endDate = '2021-01-01'

# Pull in data via EIA API
for i in range(len(PADD_KEY)):
    url = 'http://api.eia.gov/series/?api_key=' + api_key +'&series_id=' + PADD_KEY[i]
    
    r = requests.get(url)
    json_data = r.json()
    
    if r.status_code == 200:
        print('Success!')
    else:
        print('Error')
    
    df = pd.DataFrame(json_data.get('series')[0].get('data'),
                      columns = ['Date', PADD_NAMES[i]])
    
    df.set_index('Date', drop=True, inplace=True)
    
    final_data.append(df)
    
    
# Combine all the data into one dataframe
crude = pd.concat(final_data, axis=1)

# Create date as datetype datatype
crude['Year'] = crude.index.astype(str).str[:4]

crude['Month'] = crude.index.astype(str).str[4:]

crude['Day'] = 1

crude['Date'] = pd.to_datetime(crude[['Year','Month','Day']])

crude.set_index('Date',drop=True,inplace=True)

crude.sort_index(inplace=True)

crude = crude[startDate:endDate]

crude = crude.iloc[:,:5]

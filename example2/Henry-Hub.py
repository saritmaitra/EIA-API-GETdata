import json
import numpy as np
import pandas as pd
from urllib.error import URLError, HTTPError
from urllib.request import urlopen
import eia


# Henry Hub Spot Price, Daily (Release Date: 3/11/2020; Next Release Date: 3/18/2020 )
print('\033[4mHenry Hub Natural Gas Spot Price, Daily (Dollars per Million Btu)\033[0m')
def retrieve_time_series(api, series_ID):
    """
    Return the time series dataframe, based on API and unique Series ID
    """
    #Retrieve Data By Series ID 
    series_search = api.data_by_series(series=series_ID)
    ##Create a pandas dataframe from the retrieved time series
    HenryHubSpot = pd.DataFrame(series_search)
    return HenryHubSpot

def main():
    """
    Run main script
    """
    try:
      #Create EIA API using your specific API key
      api_key = "xxxxxx"
      api = eia.API(api_key)
      #Declare desired series ID
      series_ID='NG.RNGWHHD.D'
      HenryHubSpot = retrieve_time_series(api, series_ID)
      #Print the returned dataframe df
      print(type(HenryHubSpot))
      return HenryHubSpot;
    except Exception as e:
      print("error", e)
      return pd.DataFrame(columns=None)

HenryHubSpot = main()
HenryHubSpot = HenryHubSpot.rename({'Henry Hub Natural Gas Spot Price, Daily (Dollars per Million Btu)': 'spotPrice'}, axis = 'columns')
HenryHubSpot = HenryHubSpot.reset_index()
HenryHubSpot['index'] = pd.to_datetime(HenryHubSpot['index'].str[:-3], format='%Y %m%d')
HenryHubSpot['Date']= pd.to_datetime(HenryHubSpot['index']) 
HenryHubSpot.set_index('Date', inplace=True) # setting index column
HenryHubSpot = HenryHubSpot.loc['2000-01-01':,['spotPrice']] # setting date range
HenryHubSpot = HenryHubSpot.astype(float)
print(HenryHubSpot) 

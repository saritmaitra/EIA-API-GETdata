import json
import numpy as np
import pandas as pd
from urllib.error import URLError, HTTPError
from urllib.request import urlopen
import eia


def retrieve_time_series(api, series_ID):
    """
    Return the time series dataframe, based on API and unique Series ID
    """
    # Retrieve Data By Series ID
    series_search = api.data_by_series(series=series_ID)
    # Create a pandas dataframe from the retrieved time series
    hh_spot = pd.DataFrame(series_search)
    return hh_spot


def main():
    """
    Run main script
    """
    try:
        # Create EIA API using your specific API key
        api_key = "xxxxx"
        api = eia.API(api_key)
        # Declare desired series ID
        series_ID = 'NG.RNGWHHD.W'
        hh_spot = retrieve_time_series(api, series_ID)
        # Print the returned dataframe df
        print(type(hh_spot))
        return hh_spot
    except Exception as e:
        print("error", e)
        return pd.DataFrame(columns=None)


hh_spot = main()
hh_spot = hh_spot.rename(
    {'Henry Hub Natural Gas Spot Price, Weekly (Dollars per Million Btu)': 'hh_spot'}, axis='columns')
hh_spot = hh_spot.reset_index()
hh_spot['index'] = pd.to_datetime(hh_spot['index'].str[:-3], format='%Y %m%d')
hh_spot['Date'] = pd.to_datetime(hh_spot['index'])
hh_spot.set_index('Date', inplace=True)  # setting index column
hh_spot = hh_spot.loc['2000-01-01':, ['hh_spot']]  # setting date range
hh_spot = hh_spot.astype(float)
print(hh_spot)

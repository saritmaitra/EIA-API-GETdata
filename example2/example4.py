# Weekly Lower 48 States Natural Gas Working Underground Storage, Weekly
print('\033[4mWeekly Lower 48 States Natural Gas Working Underground Storage, Weekly\033[0m')
def retrieve_time_series(api, series_ID):
    """
    Return the time series dataframe, based on API and unique Series ID
    """
    #Retrieve Data By Series ID 
    series_search = api.data_by_series(series=series_ID)
    ##Create a pandas dataframe from the retrieved time series
    stor_wk = pd.DataFrame(series_search)
    return stor_wk

def main():
    """
    Run main script
    """
    try:
      #Create EIA API using your specific API key
      api_key = "xxxx"
      api = eia.API(api_key)
      #Declare desired series ID
      series_ID='NG.NW2_EPG0_SWO_R48_BCF.W'
      stor_wk = retrieve_time_series(api, series_ID)
      #Print the returned dataframe df
      print(type(stor_wk))
      return stor_wk;
    except Exception as e:
      print("error", e)
      return pd.DataFrame(columns=None)

stor_wk = main()
stor_wk = stor_wk.rename({
    'Weekly Lower 48 States Natural Gas Working Underground Storage, Weekly (Billion Cubic Feet)': 
    'stor_wk'}, axis = 'columns')
stor_wk = stor_wk.reset_index()
stor_wk['index'] = pd.to_datetime(stor_wk['index'] .str[:-3], format='%Y %m%d')
stor_wk['Date']= pd.to_datetime(stor_wk['index']) 
stor_wk.set_index('Date', inplace=True) # setting index column
stor_wk = stor_wk.loc['2010-01-01':,['stor_wk']] # setting date range
stor_wk = stor_wk.astype(float)
stor_wk = stor_wk.resample('B').ffill()
stor_wk = stor_wk/21

import eia
import pandas as pd

def retrieve_time_series(api, series_ID):
    """
    Return the time series dataframe, based on API and unique Series ID
    """
    #Retrieve Data By Series ID 
    series_search = api.data_by_series(series=series_ID)
    ##Create a pandas dataframe from the retrieved time series
    df = pd.DataFrame(series_search)
    return df

def main():
    """
    Run main script
    """
    #Create EIA API using your specific API key
    api_key = "API KEY HERE"
    api = eia.API(api_key)
    #Declare desired series ID
    series_ID='EMISS.CO2-TOTV-TT-NG-TX.A'
    df=retrieve_time_series(api, series_ID)
    #Print the returned dataframe df
    print(df)

if __name__== "__main__":
    main()

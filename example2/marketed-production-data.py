import pandas as pd
import eia

# U.S. Natural Gas Marketed Production, Monthly
print('\033[4mNatural Gas Marketed Production, Monthly (Million Cubic Feet)\033[0m')


def retrieve_time_series(api, series_ID):
    """
    Return the time series dataframe, based on API and unique Series ID
    """
    # Retrieving Data By Series ID
    series_search = api.data_by_series(series=series_ID)

    # Creating pandas dataframe from the retrieved time series
    MarketedProduction = pd.DataFrame(series_search)

    return MarketedProduction


def main():
    """
    Run main script
    """
    try:
        # Create EIA API using your specific API key
        api_key = "ad819ee5a69e69390eadf300fa168fa8"
        api = eia.API(api_key)

        # series ID
        series_ID = 'NG.N9050US2.M'

        MarketedProduction = retrieve_time_series(api, series_ID)

        # Print the returned dataframe df
        print(type(MarketedProduction))
        return MarketedProduction

    except Exception as e:
        print("error", e)
        return pd.DataFrame(columns=None)


MarketedProduction = main()

MarketedProduction = MarketedProduction.rename(
    {'U.S. Natural Gas Marketed Production, Monthly (Million Cubic Feet)': 'MarketedProductuon'}, axis='columns')

MarketedProduction = MarketedProduction.reset_index()

MarketedProduction['Date'] = pd.to_datetime(MarketedProduction['index'])

MarketedProduction.set_index('Date', inplace=True)  # setting index column
# setting date range
MarketedProduction = MarketedProduction.loc['2010-01-01':, ['prod']]

prod = MarketedProduction.astype(float)

MarketedProduction = MarketedProduction.resample('B').ffill()

MarketedProduction = MarketedProduction/21

print(MarketedProduction)

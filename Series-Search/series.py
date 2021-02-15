import eia

api_key = "YOUR_API-KEY"
api = eia.API(api_key)

### Search By Keyword ###
# set return_list to True if you only want a list of data series names.
# filters_to_keep and filters_to_remove filter the search results, and 
# keep or delete, respectively, search results which contain filtered words.
keyword_search = api.search_by_keyword(keyword=['crude oil', 'price'],
                                       filters_to_keep=['AEO2015'],
                                       filters_to_remove=['high price'],
                                       rows=1000, 
                                       return_list=False)

for key, value in keyword_search.items():
    print(key, value)


### Search By Category ID ###
# set return_list to True if you only want a list of data series names
category_search = api.search_by_category(category=2,
                                         filters_to_keep=['Alabama'],
                                         filters_to_remove=['quarterly'],
                                         return_list=False)

for key, value in category_search.items():
    print(key, value)


### Search By Date Last Updated ###
# set return_list to True if you only want a list of data series names
date_search = api.search_by_date(date='2014-01-01T00:00:00Z TO 
                                       2015-01-01T23:59:59Z',
                                 filters_to_keep=['Arkansas'],
                                 filters_to_remove=['annual'],
                                 rows=1000, 
                                 return_list=True)

for result in date_search:
    print(result)

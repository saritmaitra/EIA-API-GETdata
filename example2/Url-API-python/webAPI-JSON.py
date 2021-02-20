import sys
import requests
import eia

# Json format
link = "http://api.eia.gov/series/?series_id=NG.N9010US2.M&api_key=xxxx&out=json"
f = requests.get(link)
print(f.text)

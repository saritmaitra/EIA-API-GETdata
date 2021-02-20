import sys
import requests
import eia

#pip install eia-python

# XML format
link = "http://api.eia.gov/series/?series_id=NG.N9010US2.M&api_key=xxxxx&out=xml"
f = requests.get(link)
print(f.text)




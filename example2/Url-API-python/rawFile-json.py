import requests

x = requests.get("https://sarit-maitra.medium.com/")
print(x.status_code)

# XML format
link = "http://api.eia.gov/series/?series_id=NG.N9010US2.M&api_key=xxxxx&out=xml"
f = requests.get(link)
print(f.text)

# Json format
link = "http://api.eia.gov/series/?series_id=NG.N9010US2.M&api_key=xxxx&out=json"
f = requests.get(link)
print(f.text)

link = "http://api.eia.gov/category/?api_key=xxxxx"
f = requests.get(link)
print(f.text)

link = "http://api.eia.gov/series/categories/?series_id=xxxx&api_key=xxxx"
f = requests.get(link)
print(f.text)


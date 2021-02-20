
link = "http://api.eia.gov/category/?api_key=xxxxx"
f = requests.get(link)
print(f.text)

link = "http://api.eia.gov/series/categories/?series_id=xxxx&api_key=xxxx"
f = requests.get(link)
print(f.text)

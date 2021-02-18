import requests

link = "http://api.eia.gov/series/?series_id=series_id&api_key=xxxxx"
f = requests.get(link)
print(f.text)

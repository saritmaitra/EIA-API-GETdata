import sys
import requests
import os
import math

# print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello. {}".format(who_to_greet)
    return greeting


# print(greet('Sarit'))
# print(greet('Maitra'))

x = requests.get("https://sarit-maitra.medium.com/")
print(x.status_code)

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


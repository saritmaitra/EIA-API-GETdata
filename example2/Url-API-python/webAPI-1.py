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


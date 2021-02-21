import sys
import requests  # requests library handles SSL certificate verification for you
import os
import math
from string import Template

"""f-strings are interesting; but as flexibility increases, so does the potential for exploits
We have used string format here which is a bit cumbersome because it requires an import statement and it is less flexible with types. 
It also doesn’t evaluate Python statements the way f-strings do. 
These constraints make template strings an excellent choice when dealing with user input."""

# print(sys.version)
print(sys.executable)

greeting_template = Template("Hello World, my name is $name.")
greeting = greeting_template.substitute(name="Sarit Maitra")
print(greeting)


def greet(who_to_greet):
    greeting = "Hello. {}".format(who_to_greet)
    return greeting


# print(greet('Sarit'))
# print(greet('Maitra'))

x = requests.get("https://sarit-maitra.medium.com/")
print(x.status_code)


import json
import requests

r = requests.get("https://formulae.brew.sh/api/formula.json")
packages_json = r.json()

for package in packages_json:
    package_name = package["name"]
    package_desc = package["desc"]

    package_url = f"https://formulae.brew.sh/api/formula/{package_name}.json"

    r = requests.get(package_url)
    package_json = r.json()

    installs_30 = package_json["analytics"]["install_on_request"]["30d"][package_name]
    installs_90 = package_json["analytics"]["install_on_request"]["90d"][package_name]
    installs_365 = package_json["analytics"]["install_on_request"]["365d"][package_name]

    print(package_name, package_desc, installs_30, installs_90, installs_365)


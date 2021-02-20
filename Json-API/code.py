import json
import requests

r = requests.get("https://formulae.brew.sh/api/formula.json")
packages_json = r.json()

print(len(packages_json))

# print(packages_json)

# package_name = packages_json[0]["name"]
# package_desc = packages_json[0]["desc"]
# package_url = f"https://formulae.brew.sh/api/formula/{package_name}.json"
# r = requests.get(package_url)
# package_json = r.json()
# package_str = json.dumps(package_json, indent=2)
# print(package_str)

# installs_30 = package_json["analytics"]["install_on_request"]["30d"][package_name]
# installs_90 = package_json["analytics"]["install_on_request"]["90d"][package_name]
# installs_365 = package_json["analytics"]["install_on_request"]["365d"][package_name]
# print(package_name, package_desc, installs_30, installs_90, installs_365)

# packaages_str = json.dumps(packages_json[0], indent=2)
# print(packaages_str)

# https://formulae.brew.sh/api/formula/a2ps.json

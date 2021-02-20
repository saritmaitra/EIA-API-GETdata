import json

with open("package_info.json", "r") as f:
    data = json.load(f)

#print(data)

def install_sort(package):
    return package['analytics']['30d']
    
data = [item for item in data if 'video' in item ['desc']]
data.sort(key=install_sort, reverse = True)

data_str = json.dumps(data, indent=2)

print(data_str)

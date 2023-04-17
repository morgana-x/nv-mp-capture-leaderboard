import requests
import json


discordcookie = "web:discordlogin=INSERTJUNKHERE"

h = {"cookie": discordcookie}

r = requests.get('https://nv-mp.com/eden/api/grouplist.json', headers = h)

def getMembers(d):
    return int(d["num_zones_owned"])

data = json.loads(r.text)

data.sort(key=getMembers)

for group in data:
    if group["num_zones_owned"] <= 0:
        continue
    print(group["name"] + ": " + str(group["num_zones_owned"])) 

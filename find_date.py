import requests

fourm = "2019_ncov"
last_id = 235807353
api = "https://www.dcard.tw/_api/forums/"+fourm+"/posts?popular=false&limit=100&before=" + str(last_id)

request = requests.get(api)
request = request.json()

for i in range(len(request)):
    print(request[i]['id'])
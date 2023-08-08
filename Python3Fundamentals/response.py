import requests

city = ' '
url = ' '+city+''

response = requests.get(url)
responseJson = response.json()
print(responseJson)

curTemp = responseJson.get('current').get('temp__f')
description = responseJson.get('current').get('condition').get('text')

print(city,'Currently',description,'with',curTemp,'degrees')

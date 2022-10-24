import requests
import json

response = requests.get('http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

#print(response) will print status number eg 404
#print(response.json())#will print data
#print(response.json()['items'])#prints items specifically

for data in response.json()['items']:
    #print(data['title'])
    print(data['link'])

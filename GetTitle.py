import requests
import json
import pandas as pd

url = "https://auth.emsicloud.com/connect/token"
payload = {
    'client_id': 'jb8buspllvp5yvm2',
    'client_secret': 'am3FJllo',
    'grant_type': 'client_credentials',
    'scope': 'emsi_open'
}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
response = requests.post(url=url, data=payload, headers=headers)

response_dict = json.loads(response.text)
auth = 'Bearer ' + response_dict['access_token']

url = "https://emsiservices.com/titles/versions/latest/titles"

querystring = {"q":".NET", "limit" : "5", "page":"2"}
headers = {'Authorization': auth}

response = requests.request("GET", url, headers=headers)
allTitles_set = json.loads(response.text)['data']

allTitles = pd.DataFrame(allTitles_set)
allTitles.to_excel('allTitles.xlsx')



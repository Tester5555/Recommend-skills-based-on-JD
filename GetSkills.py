import json
import requests
import pandas as pd
import openpyxl

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

url = "https://emsiservices.com/skills/versions/latest/skills"

# querystring = {"q":".NET","typeIds":"ST1,ST2","fields":"id,name,type,infoUrl"}

headers = {'Authorization': auth}

response = requests.request("GET", url, headers=headers)

allSkills_set = json.loads(response.text)['data']
#print(allSkills_set)

allSkills = pd.DataFrame(allSkills_set)
allSkills.to_excel('allSkills.xlsx')
#print(allSkills)

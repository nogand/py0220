import requests
import configparser
import os

config=configparser.ConfigParser()
config.read(os.environ.get("CONFIGFILE","./apigithub.ini"))
TOKEN = os.environ.get("TOKENGH", config.get("autenticacion","token"))

with requests.Session() as session:
  headers = {'Authorization': 'token ' + TOKEN}
  response = session.get('https://api.github.com/user', headers=headers)

print(response.headers)
print(response.json())

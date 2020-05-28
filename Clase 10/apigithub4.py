import requests
import configparser
import os

config=configparser.ConfigParser()
config.read(os.environ.get("CONFIGFILE","./apigithub.ini"))
USUARIO = os.environ.get("USUARIOGH", config.get("autenticacion","usuario"))
TOKEN = os.environ.get("TOKENGH", config.get("autenticacion","token"))

with requests.Session() as session:
  session.auth = (USUARIO,TOKEN)
  response = session.get('https://api.github.com/user')

print(response.headers)
print(response.json())

import requests
import configparser
import os

config=configparser.ConfigParser()
config.read(os.environ.get("CONFIGFILE","./apigithub.ini"))
USUARIO = os.environ.get("USUARIOGH", config.get("autenticacion","usuario"))
CLAVE = os.environ.get("CLAVEGH", config.get("autenticacion","clave"))

with requests.Session() as session:
  session.auth = (USUARIO,CLAVE)
  response = session.get('https://api.github.com/user')

print(response.headers)
print(response.json())

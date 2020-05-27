import requests
from getpass import getpass

with requests.Session() as session:
  session.auth = ('nogand', getpass())
  response = session.get('https://api.github.com/user')

print(response.headers)
print(response.json())

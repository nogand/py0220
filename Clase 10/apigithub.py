import requests
from getpass import getpass

response=requests.get('https://api.github.com/user', auth=('nogand', getpass()))

print(response.headers)
print(response.json())

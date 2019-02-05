import requests

url = 'http://127.0.0.1:3000/'

resp = requests.get(url + 'HelloWorld')
print(resp.text)

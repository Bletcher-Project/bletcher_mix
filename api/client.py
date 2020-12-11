import requests

URL = "http://127.0.0.1:8000"

data = {'content_url': 'dog', 'style_url': 'crying'}
res = requests.post(URL, data=data)
print(res)
import requests

r = requests.get('https://api.github.com/events')

# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('http://httpbin.org/get', params=payload)
# print(r.url)

print(r.text)
r.content

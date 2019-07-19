import requests
url = "http://example.com"
response = requests.get(url)
response.encoding = response.apparent_encoding
print(response.text)

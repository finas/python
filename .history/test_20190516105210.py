import requests
import re


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get('https://tvc4.forexpros.com/',headers=headers)
carrier = re.findall('carrier=([^&]+)', response.text)[0]

print(response)

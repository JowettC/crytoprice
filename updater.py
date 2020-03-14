
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
# api key is basic key which is free, limited
f= open("test.json","w+")
f.close()
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'acb28213-8883-471f-8bf2-2d65048a5e0b',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  f= open("data.json","w+")
  f.write(json.dumps(data))
  print("SUCCESS")
  f.close()
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

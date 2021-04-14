import requests
import json

url = 'https://api.swanfinance.io/api/v1/signup/local'
body = {"fullName":"Jerry","secondName":"Potson","email":"fowrov@mailmax.space","password":"S3JUoZlt0si","rfcode":"","termsAccepted":'true',"isUs":'true',"captcha":'null',"channel":""}
headers = {
  'Referrer Policy': 'strict-origin-when-cross-origin',
  'authority': 'api.swanfinance.io',
  'method': 'POST',
  'path': '/api/v1/signup/local',
  'scheme': 'https',
  'accept': 'application/json, text/plain, */*',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'en',
  'content-length': '177',
  'content-type': 'application/json;charset=UTF-8',
  'origin': 'https://app.swanfinance.io',
  'referer': 'https://app.swanfinance.io/',
  'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}

r = requests.post(url, data=json.dumps(body), headers=headers)
print(r)
print(r.text)
#Rezult vyvesti v txt fayl
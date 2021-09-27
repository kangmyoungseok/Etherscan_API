from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import pandas as pd
import json
from bs4 import BeautifulSoup
import re # 추가
from urllib.request import urlopen
import requests


csv_test = pd.read_csv('./total_v1.1.csv')
datas = csv_test.to_dict('records')
print(datas[0])

token = 'EK-4L18F-Y2jC1b7-9qC3N'
url = 'https://api.ethplorer.io/getTokenHistory/'

data = datas[0]
print(line)
for data in datas:
    line = data['platform.token_address']
    url1 = 'https://api.ethplorer.io/getTokenHistory/' + line + '?apiKey='+ token
    response1 = json.loads(requests.get(url).text)

    url2 = 'https://api.ethplorer.io/getTokenHistoryGrouped/' + line + '?apikey' + token    
    response2 = json.loads(requests.get(url).text)

response2['operations'][0].keys()






response['operations'][0]
#csv_test = pd.read_csv('result.csv')
#datas = csv_test.to_dict('records')
# https://api.ethplorer.io/getTokenInfo/0x7f3edcdd180dbe4819bd98fee8929b5cedb3adeb?apiKey=EK-4L18F-Y2jC1b7-9qC3N
token = 'EK-4L18F-Y2jC1b7-9qC3N'
#for data in datas:
line = '0x154e35c2b0024B3e079c5c5e4fC31c979c189cCB'  
print (line)
repos_url = 'https://api.ethplorer.io/getTokenHistory/'+line+'?apiKey='+token
gh_session = requests.Session()

repos = json.loads(gh_session.get(repos_url).text) # json으로 뽑아오자  
print(repos)
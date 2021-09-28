from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import pandas as pd
import json
from bs4 import BeautifulSoup
import re # 추가
from urllib.request import urlopen
import requests
import datetime
from multiprocessing import Pool
from tqdm import tqdm


def proc(data):
    # 가장 최근 Transaction
    try:
        token_address = data['platform.token_address']
        url1 = 'https://api.ethplorer.io/getTokenHistory/'+ token_address +'?apiKey=EK-4L18F-Y2jC1b7-9qC3N' 
    #    url1 = "https://api.ethplorer.io/getTokenHistory/0xda4c27a9fbdde1f5f3af0398396be4644dcec715?apiKey=freekey"
        response1 = json.loads(requests.get(url1).text)
        unixtime = response1['operations'][0]['timestamp']
        date = datetime.datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d %H:%M:%S')

        # 30일 동안 거래가 있는 날짜 갯수
        url2 = 'https://api.ethplorer.io/getTokenHistoryGrouped/'+ token_address +'?apiKey=EK-4L18F-Y2jC1b7-9qC3N' 
    #    url2 = "https://api.ethplorer.io/getTokenHistoryGrouped/0x73dd33350be2c7b36cd653f0344307b5186c4f84?apiKey=EK-4L18F-Y2jC1b7-9qC3N"
        response2 = json.loads(requests.get(url2).text)
        count_date = len(response2['countTxs'])

        # 30일 동안 거래 transaction 평균 
        count = 0
        for Txs in response2['countTxs']:
            count = count + int(Txs['cnt'])
    except Exception as e:
        print(e)
        return token_address, -1, -1, -1
    
    return token_address, date, count_date, count


if __name__=='__main__':
    csv = pd.read_csv('./total_v1.3.csv')
    datas = csv.to_dict('records')
    
    token_address, date, count_date, count = [],[],[],[]
    len(datas)

    for i in tqdm(range(len(datas))):
        result = proc(datas[i])
        token_address.append(result[0])
        date.append(result[1])
        count_date.append(result[2])
        count.append(result[3])

    data = {
        'token_address' : token_address,
        'date' : date,
        'count_date' : count_date,
        'count' : count
    }

    df = pd.DataFrame(data)
    df.to_csv('result.csv')






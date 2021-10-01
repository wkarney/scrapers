'''
Scraper for brewers association data
'''
import json

import pandas as pd
import requests

def pull_ba_data():
    r = requests.get(url='https://www.brewersassociation.org/wp-content/themes/ba2019/json-store/breweries/breweries.json')
    json_data = json.loads(r.json())
    df = pd.DataFrame(json_data['ResultData'])
    return df

if __name__ == '__main__':
    pull_ba_data().to_csv('./data/ba_brewery_data.csv',index=False)
    
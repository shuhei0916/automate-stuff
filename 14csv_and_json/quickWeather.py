# コマンドラインに指定した地名の天気予報を表示する

import json, requests, sys

# コマンドライン引数から地名を組み立てる
if len(sys.argv) < 2:
    print('Usage: quichWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# openweathermap.orgから取得したAPIキーを定義しておく
APPID = '07a52d6f6892d9e0e88c3ab60573753f'

# TODO: OpenWeatherMap.orgのAPIからJSONデータをダウンロードする
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q={}&cnt=3&appid={}'.format(location, APPID)
url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&cnt=3&appid={APPID}'
response = requests.get(url)
response.raise_for_status()
print(response)

# TODO: JSONデータからPython変数に読み込む
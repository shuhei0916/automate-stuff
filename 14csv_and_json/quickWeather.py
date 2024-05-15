# コマンドラインに指定した地名の天気予報を表示する

import json, requests, sys
import pprint

# コマンドライン引数から地名を組み立てる
if len(sys.argv) < 2:
    print('Usage: quichWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# openweathermap.orgから取得したAPIキーを定義しておく
APPID = '07a52d6f6892d9e0e88c3ab60573753f'

# TODO: OpenWeatherMap.orgのAPIからJSONデータをダウンロードする
# url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q={}&cnt=3&appid={}'.format(location, APPID) # 本の通りだと401エラーが出るので修正
url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&cnt=3&appid={APPID}'
response = requests.get(url)
response.raise_for_status()


# TODO: JSONデータからPython変数に読み込む
weather_data = json.loads(response.text)
# pprint.pprint(weather_data)
# 天気予報の情報を表示する
w = weather_data['list']
# pprint.pprint(w)
print(f'{location}の今日の天気: ')
print(' ' + w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print(' 体感温度' + str(w[0]['main']['feels_like'] - 273.15) + '℃')
print()
print(f'{location}の明日の天気: ')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print(' 体感温度' + str(w[1]['main']['feels_like'] - 273.15) + '℃')
print()
print(f'{location}の明後日の天気: ')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
print(' 体感温度' + str(w[2]['main']['feels_like'] - 273.15) + '℃')
print()

# feels_like = w[0]['main']['feels_like'] - 273.15
# print(type(w[0]['main']['feels_like']))
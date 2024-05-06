# lucly.py Googleの検索結果をいくつか開く

import requests, sys, webbrowser, bs4

# ユーザーエージェントを設定（Chromeの例）
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


print('Googling...')
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))


res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
link_elems = soup.select('.r a')
print(link_elems)
# downloadXkcd.py XKCDコミックをひとつづつダウンロードする

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # download pages
    print('downloading pages {}...'.format(url))
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # 
    comic_elem = soup.select('#comic img')
    if comic_elem == []:
        print('cannot find comic img')
    else:
        comic_url = 'http:' + comic_elem[0].get('src')
        # download the image
        print('downloading the image {}...'.format(comic_url))
        res = requests.get(comic_url)
        res.raise_for_status()

        # save images
        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
        for chunk in res.iter_content(10000):
            image_file.write(chunk)
        image_file.close()
        
    # get prev button's URL
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')
    
print('finished')


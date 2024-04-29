import requests

res = requests.get('https://inventwithpython.com//page_that_does_not_exit')
try:
    res.raise_for_status()
except Exception as e:
    print('Problem exits: {}'.format(e))
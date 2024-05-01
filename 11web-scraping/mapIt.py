#! python3
# mapIt.py - コマンドラインやクリップボードに指定した住所の地図を開く

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # get address from commandline
    address = ' '.join(sys.argv[1:])
else:
    # TODO: get address from clipboard
    address = pyperclip.paste()


print(address)
webbrowser.open('https://www.google.com/maps/place/' + address)

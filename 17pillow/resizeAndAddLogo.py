import os 
from PIL import Image

# カレントディレクトリの全ての画像を300*300に収まるようにサイズ変更し、
# catlogo.pngを右下に追加する。

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = './17pillow/catlogo.png'

logo_im = Image.open(LOGO_FILENAME)
logo_width, logo_height = logo_im.size

# print(logo_height, logo_width)

os.makedirs('./17pillow/withlogo', exist_ok=True)

# TODO: カレントディレクトリの全画像をループする
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME: # あれ？複数行にまたがって書くのってバックスラッシュじゃなかったっけ？
        continue
    
    im = Image.open(filename)
        
    

# TODO: 画像をサイズ変更する
# TODO: ロゴを追加する
# TODO: 変更を保存する
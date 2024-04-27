# renameDates.py 米国式日付MM-DD-YYYYのファイル名を欧米式DD-MM-YYYYに変換

import shutil, os, re

# 米国式日付のファイル名にマッチする正規表現を作る
date_pattern = re.compile(r"""^(.*?)
                          ((0|1)?\d)-
                          ((0|1|2|3)?\d)-
                          ((19|20)\d\d)
                          (.*?)$
                          """, re.VERBOSE)


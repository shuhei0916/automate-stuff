# ランダム順に問題と答えを並べ問題集と回答集を作る

import random

capitals = {'北海道': '札幌市', '青森県': '青森市', '岩手県': '盛岡市', '宮城県': '仙台市'}

for quis_num in range(3):
    # TODO: 問題集と回答集のファイルを作成する
    quiz_file = open('capitalsquiz{}.txt'.format(quiz_num + 1), )
    # TODO: 問題集のヘッダーを書く
    # TODO: 都道府県の順番をシャッフルする
    # TODO: 47都道府県をループして、それぞれ問題を作成する
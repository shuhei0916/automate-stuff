import random
guess = ''
while guess not in ('1', '0'):
    print('コインの裏表を当ててください。裏(0)か表(1)を入力してください')
    guess = input()
toss = random.randint(0, 1) #
if str(toss) == guess:
    print('あたり！')
else:
    print('はずれ！もう一回当てて！')
    guess = input()
    if str(toss) == guess:
        print('あたり')
    else:
        print('はずれ。このゲームは苦手ですね')

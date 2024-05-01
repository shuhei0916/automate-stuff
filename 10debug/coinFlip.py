import random
heads = 0
for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads = heads + 1
    if i == 500:
        print('半分終了！')
print('表は' + str(heads) + '回出ました。')

import os 
# 疑似的なtreeコマンド作れそう

for foldername, subfolders, filenames in os.walk('C:\\Users\\Ito\\coding\\automate-stuff'):
    if '.git' in foldername:
        continue

    print(foldername)

    for subfolder in subfolders:
        print('   ---' + subfolder)

    for filename in filenames:
        print('   ' + filename)

    print('')
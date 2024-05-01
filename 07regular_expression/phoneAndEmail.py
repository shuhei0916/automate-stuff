import pyperclip, re

phone_regex = re.compile(r'''(
                         (\d{1,4}|\(\d{1,4}\)) # 市外局番
                         (\s|-)
                         (\d{1,4})
                         (\s|-)
                         (\d{3,4})
                         (\s*(ext|x|ext.)\s*(\d{2,5}))?
                        #  (\s*(ext|x|ext\.)\s*(\d{2,5}))?  # 内線番号（オプション）
                         )''', re.VERBOSE)

# TODO: make regex for email
email_regex = re.compile(r'''(
                         [a-zA-Z0-9._%+-]+
                         @
                         [a-zA-Z0-9.-]+
                         (\.[a-zA-Z]{2,4})    
                         )''', re.VERBOSE)

# TODO: search the clipboarded text
text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])

# TODO: paste the result
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('クリップボードにコピーしました：')
    print('\n'.join(matches))
else:
    print('電話番号やメールアドレスは見つかりませんでした。')